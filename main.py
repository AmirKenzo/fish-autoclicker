import ctypes
import logging
import time
from dataclasses import dataclass
from threading import Thread
from typing import Any, Dict, List, Optional, Sequence, Tuple

import cv2
import dxcam
import keyboard
import numpy as np
import pydirectinput
import toml
import winsound


pydirectinput.FAILSAFE = False
LOGGER = logging.getLogger(__name__)

VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
KEYEVENTF_KEYUP = 0x0002


class ConfigError(RuntimeError):
    """Raised when the configuration file is invalid."""


@dataclass
class Region:
    left: int
    top: int
    width: int
    height: int

    @property
    def right(self) -> int:
        return self.left + self.width

    @property
    def bottom(self) -> int:
        return self.top + self.height


@dataclass
class BoxRecord:
    center: Tuple[int, int]
    color: Tuple[int, int, int]
    bounds: Tuple[int, int, int, int]


def press_key(vk_code: int) -> None:
    user32 = ctypes.windll.user32
    user32.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.01)
    user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)


def load_template(path: str) -> np.ndarray:
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        raise ConfigError(f"Template '{path}' could not be loaded.")
    return template


class NewMiniGame:
    RESET = 0
    FOUND = 1
    INTERCEPTION = 2

    def __init__(self, config: Dict[str, Any]) -> None:
        mini_cfg = config["new_minig_game"]
        self.state = self.RESET
        self.starting_area = 0
        self.prev_area = 0
        self.number = 0
        self.number_reset_flag = False  # Flag to force reset number on next detection
        self.vk_keys = [VK_1, VK_2, VK_3, VK_4]

        region_cfg = mini_cfg["main_region"]
        self.zone = Region(
            left=region_cfg["left"],
            top=region_cfg["top"],
            width=region_cfg["width"],
            height=region_cfg["height"],
        )

        number_cfg = mini_cfg["number_region"]
        self.number_zone = Region(
            left=number_cfg["left"] - self.zone.left,
            top=number_cfg["top"] - self.zone.top,
            width=number_cfg["width"],
            height=number_cfg["height"],
        )

        self.minimum_pixel = mini_cfg["filter_noise"]
        self.number_conf = mini_cfg["number_conf"]
        self.compare_dif = mini_cfg["compare_dif"]
        self.new_area_diff = mini_cfg["new_area_diff"]
        self.number_threshold = mini_cfg["number_threshold"]
        bar_cfg = mini_cfg["bar"]
        self.rgb_color_lower = np.array(bar_cfg["rgb_color_lower"], dtype=np.uint8)
        self.rgb_color_upper = np.array(bar_cfg["rgb_color_upper"], dtype=np.uint8)
        self.templates = [load_template(f"asset/{name}") for name in ("n1", "n2", "n3")]

    def _crop_zone(self, frame: np.ndarray) -> np.ndarray:
        return frame[
            self.zone.top : self.zone.bottom,
            self.zone.left : self.zone.right,
        ]

    def _detect_number(self, roi: np.ndarray) -> None:
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, self.number_threshold, 255, cv2.THRESH_BINARY)
        best_score = -1.0
        detected = 0
        all_scores = []

        for idx, template in enumerate(self.templates):
            result = cv2.matchTemplate(mask, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)
            all_scores.append((idx + 1, max_val))
            if max_val >= self.number_conf and max_val > best_score:
                best_score = max_val
                detected = idx + 1

        # If no number meets the confidence threshold, use the one with highest score anyway
        # This helps with numbers that have lower confidence (like 3)
        if not detected and all_scores:
            best_idx, best_val = max(all_scores, key=lambda x: x[1])
            if best_val >= 0.35:  # Minimum threshold even if below number_conf
                detected = best_idx
                best_score = best_val

        # If reset flag is set, clear number first
        if self.number_reset_flag:
            self.number = 0
            self.number_reset_flag = False
        
        # Always update number if detected
        if detected:
            old_number = self.number
            self.number = detected
            if old_number != detected:
                scores_str = ", ".join([f"Num{n}={s:.3f}" for n, s in all_scores])
                LOGGER.info(f"[MINIGAME] DETECTED: Number {detected} (confidence: {best_score:.3f}) | Scores: [{scores_str}]")
        else:
            if self.number != 0:
                scores_str = ", ".join([f"Num{n}={s:.3f}" for n, s in all_scores])
                LOGGER.warning(f"[MINIGAME] NOT DETECTED: No valid number found (previous: {self.number}) | Scores: [{scores_str}]")
            # Don't reset to 0 if nothing detected - keep previous value

    def run(self, frame: np.ndarray) -> bool:
        zone_image = self._crop_zone(frame)
        zone_image = cv2.cvtColor(zone_image, cv2.COLOR_RGB2BGR)
        mask = cv2.inRange(zone_image, self.rgb_color_lower, self.rgb_color_upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = [cnt for cnt in contours if cv2.contourArea(cnt) > self.minimum_pixel]
        mask[:] = 0
        cv2.drawContours(mask, contours, -1, 255, cv2.FILLED)

        current_area = int(np.sum(mask == 255))
        
        # Always try to detect number when we have an active area
        if current_area > 0:
            number_roi = zone_image[
                self.number_zone.top : self.number_zone.bottom,
                self.number_zone.left : self.number_zone.right,
            ]
            self._detect_number(number_roi)
        
        if self.state == self.FOUND and self.starting_area:
            if current_area / self.starting_area <= self.compare_dif:
                # Only transition to INTERCEPTION if we have a valid number
                if self.number > 0:
                    self.state = self.INTERCEPTION
                    area_ratio = current_area / self.starting_area
                    LOGGER.info(f"[MINIGAME] STATE: FOUND -> INTERCEPTION | Area: {current_area}/{self.starting_area} ({area_ratio:.3f}) | Number: {self.number}")
                else:
                    LOGGER.warning(f"[MINIGAME] STATE: Cannot go to INTERCEPTION - no number detected (number: {self.number})")
        elif self.state == self.RESET and current_area > 0:
            self.state = self.FOUND
            self.starting_area = current_area
            self.number_reset_flag = True  # Flag to reset number on next detection
            LOGGER.info(f"[MINIGAME] STATE: RESET -> FOUND | Area: {current_area} | Resetting number detection")
        elif current_area == 0:
            if self.state != self.RESET:
                LOGGER.info(f"[MINIGAME] STATE: {self.state} -> RESET | Area: 0")
            self.state = self.RESET
            self.starting_area = 0
            self.number = 0  # Reset number when area disappears
        elif (
            current_area != 0
            and self.state == self.FOUND
            and self.starting_area
            and current_area / self.starting_area >= self.new_area_diff
        ):
            self.starting_area = current_area

        self.prev_area = current_area

        if self.state == self.INTERCEPTION and self.number:
            vk_idx = max(0, min(len(self.vk_keys) - 1, self.number - 1))
            key_pressed = vk_idx + 1  # 1-based for logging
            LOGGER.info(f"[MINIGAME] =====> CLICKED KEY {key_pressed} <===== | Detected Number: {self.number}")
            press_key(self.vk_keys[vk_idx])
            self.state = self.RESET
            self.number = 0
            self.number_reset_flag = False  # Clear flag
            self.prev_area = 0
            self.starting_area = 0
            return True
        elif self.state == self.INTERCEPTION and not self.number:
            LOGGER.warning(f"[MINIGAME] STATE: INTERCEPTION but no number detected! (number: {self.number}) - waiting...")

        return self.state != self.RESET


class FivemAutoFish:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.new_fish_mini = NewMiniGame(config)

        self.nums = [load_template(f"asset/{name}") for name in ("d1", "d2", "d3")]
        self.BoxNumber1: Optional[BoxRecord] = None
        self.BoxNumber2: Optional[BoxRecord] = None
        self.BoxNumber3: Optional[BoxRecord] = None

        self.went_to_none = False
        self.pause = True
        self.last_no_detection = time.time()
        self.e_press_count = 0  # Counter for E key presses

        global_cfg = config["global"]
        self.last_no_detection_delay = global_cfg["last_no_detection_delay"]
        self.process_frame_number_threshold = global_cfg["process_frame_number_threshold"]
        self.process_frame_boxes_threshold = global_cfg["process_frame_boxes_threshold"]
        self.process_frame_number_conf = global_cfg["process_frame_number_conf"]
        self.click_delay = global_cfg["click_delay"]
        self.pause_key_name = global_cfg["pause_key_name"]
        self.pause_key_code = keyboard.key_to_scan_codes(self.pause_key_name)[0]
        self.cs_background_color_lower = np.array(global_cfg["cs_background_color_lower"], dtype=np.uint8)
        self.cs_background_color_upper = np.array(global_cfg["cs_background_color_upper"], dtype=np.uint8)
        self.cs_success_color = tuple(global_cfg["cs_success_color"])
        self.fish_press_e_template = load_template("asset/d4")
        self.bar_x = config["bar"]["x"]
        self.bar_y = config["bar"]["y"]
        self.fish_press_e_conf = global_cfg["fish_press_e_conf"]
        self.fish_press_e_delay = global_cfg["fish_press_e_delay"]

        monitor_cfg = config.get("monitor", 0)
        if isinstance(monitor_cfg, dict):
            self.monitor = monitor_cfg.get("index", 0)
            self.monitor_width = monitor_cfg.get("width")
            self.monitor_height = monitor_cfg.get("height")
        else:
            self.monitor = int(monitor_cfg)
            self.monitor_width = None
            self.monitor_height = None
        region_cfg = config["region"]
        self.region = Region(
            left=region_cfg["left"],
            top=region_cfg["top"],
            width=region_cfg["width"],
            height=region_cfg["height"],
        )

        self.camera = self._create_camera()
        Thread(target=self.handle_pause, daemon=True).start()
        Thread(target=self.handle_press_e, daemon=True).start()

    def _create_camera(self) -> dxcam.DXCamera:
        camera = dxcam.create(device_idx=self.monitor, output_color="RGB")
        if camera is None:
            raise RuntimeError("Failed to initialize DXCam.")
        camera.start(target_fps=60)
        return camera

    def handle_pause(self) -> None:
        while True:
            event = keyboard.read_event()
            if event.event_type == "down" and event.scan_code == self.pause_key_code:
                self.pause = not self.pause
                if self.pause:
                    LOGGER.info("Paused auto fishing")
                    winsound.Beep(1000, 200)
                else:
                    LOGGER.info("Resumed auto fishing")
                    winsound.Beep(500, 200)

    def handle_press_e(self) -> None:
        while True:
            if self.pause:
                time.sleep(0.1)
                continue

            frame = self.capture_screen_full()
            if frame is None:
                time.sleep(0.01)
                continue

            should_press = self.is_fish_press_e_available(frame) or self.is_bar_available(frame)
            if should_press:
                self.e_press_count += 1
                reason = "fish_press_e" if self.is_fish_press_e_available(frame) else "bar"
                LOGGER.info(f"[E KEY] =====> Pressed E (x2) <===== | Count: {self.e_press_count} | Reason: {reason}")
                pydirectinput.press("e")
                time.sleep(self.fish_press_e_delay)
                pydirectinput.press("e")
            else:
                time.sleep(0.02)

    def most_common_rgb_in_region(self, image_array: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> Tuple[int, int, int]:
        x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
        region = image_array[y1:y2, x1:x2]
        if region.size == 0:
            return (0, 0, 0)
        colors, counts = np.unique(region.reshape(-1, 3), axis=0, return_counts=True)
        return tuple(int(v) for v in colors[counts.argmax()])

    def capture_screen_full(self) -> Optional[np.ndarray]:
        frame = self.camera.get_latest_frame()
        return frame.copy() if frame is not None else None

    def capture_screen(self) -> Optional[np.ndarray]:
        frame = self.capture_screen_full()
        if frame is None:
            return None
        return frame[
            self.region.top : self.region.bottom,
            self.region.left : self.region.right,
        ].copy()

    def process_frame_number(self, gray_frame: np.ndarray) -> List[Dict[str, Any]]:
        _, thresh = cv2.threshold(gray_frame, self.process_frame_number_threshold, 255, cv2.THRESH_BINARY)
        detections: List[Dict[str, Any]] = []

        for idx, template in enumerate(self.nums):
            result = cv2.matchTemplate(thresh, template, cv2.TM_CCOEFF_NORMED)
            locations = np.where(result >= self.process_frame_number_conf)
            h, w = template.shape
            for pt in zip(*locations[::-1]):
                detections.append({"digit": idx + 1, "box": (pt[0], pt[1], w, h)})
        return detections

    def process_frame_boxes(self, gray_frame: np.ndarray) -> List[Dict[str, Any]]:
        _, thresh = cv2.threshold(gray_frame, self.process_frame_boxes_threshold, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        boxes: List[Dict[str, Any]] = []
        for cnt in contours:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if len(approx) != 4 or not cv2.isContourConvex(approx):
                continue
            x, y, w, h = cv2.boundingRect(approx)
            if w < 20 or h < 20:
                continue
            aspect = w / float(h)
            if not 0.8 <= aspect <= 1.2:
                continue
            boxes.append({"digit": 0, "box": (x, y, w, h)})
        return boxes

    def click_box(self, record: BoxRecord) -> None:
        abs_x = self.region.left + record.center[0]
        abs_y = self.region.top + record.center[1]
        self._click_absolute(abs_x, abs_y)

    def _click_absolute(self, x: int, y: int) -> None:
        ctypes.windll.user32.SetCursorPos(int(x), int(y))
        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
        time.sleep(self.click_delay)

    def is_bar_available(self, frame: np.ndarray) -> bool:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
        if self.bar_y >= thresh.shape[0] or self.bar_x >= thresh.shape[1]:
            return False
        return thresh[self.bar_y, self.bar_x] > 0

    def is_fish_press_e_available(self, frame: np.ndarray) -> bool:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
        result = cv2.matchTemplate(thresh, self.fish_press_e_template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= self.fish_press_e_conf)
        return len(locations[0]) > 0

    def _get_box_by_digit(self, digit: int) -> Optional[BoxRecord]:
        return {
            1: self.BoxNumber1,
            2: self.BoxNumber2,
            3: self.BoxNumber3,
        }.get(digit)

    def _set_box_by_digit(self, digit: int, record: BoxRecord) -> None:
        if digit == 1:
            self.BoxNumber1 = record
        elif digit == 2:
            self.BoxNumber2 = record
        elif digit == 3:
            self.BoxNumber3 = record

    def _update_number_boxes(self, detections: Sequence[Dict[str, Any]], frame: np.ndarray) -> None:
        for detection in detections:
            digit = detection["digit"]
            x, y, w, h = detection["box"]
            x2, y2 = x + w, y + h
            color = self.most_common_rgb_in_region(frame, x, y, x2, y2)
            color_array = np.array(color, dtype=np.uint8)
            if np.all((color_array >= self.cs_background_color_lower) & (color_array <= self.cs_background_color_upper)):
                cached = self._get_box_by_digit(digit)
                if cached:
                    color = cached.color
            center = (int(w / 2 + x), int(h / 2 + y))
            record = BoxRecord(center=center, color=color, bounds=(x, y, x2, y2))
            self._set_box_by_digit(digit, record)

    def _find_matching_box(self, color: Tuple[int, int, int]) -> Optional[BoxRecord]:
        for record in (self.BoxNumber1, self.BoxNumber2, self.BoxNumber3):
            if record and record.color == color:
                return record
        return None

    def _reset_no_detection(self) -> None:
        self.went_to_none = False
        self.last_no_detection = time.time()

    def _click_fail_safe(self, boxes: Sequence[Dict[str, Any]]) -> None:
        for box in boxes:
            x, y, w, h = box["box"]
            center_x = self.region.left + x + w // 2
            center_y = self.region.top + y + h // 2
            self._click_absolute(center_x, center_y)

    def _handle_boxes(self, boxes: Sequence[Dict[str, Any]], frame: np.ndarray) -> bool:
        success_count = 0
        clickable = False

        for box in boxes:
            x, y, w, h = box["box"]
            x2, y2 = x + w, y + h
            color = self.most_common_rgb_in_region(frame, x, y, x2, y2)

            if color == tuple(self.cs_success_color):
                success_count += 1
                continue

            clickable = True
            match = self._find_matching_box(color)
            if match:
                new_center = (int(w / 2 + x), int(h / 2 + y))
                match.center = new_center
                match.bounds = (x, y, x2, y2)

        if not clickable:
            return False

        target: Optional[BoxRecord] = None
        if success_count == 0:
            target = self.BoxNumber1
        elif success_count == 1:
            target = self.BoxNumber2
        elif success_count == 2:
            target = self.BoxNumber3

        if target:
            self.click_box(target)
            return True
        return False

    def run(self) -> None:
        LOGGER.info("Press %s to start Auto Fish", self.pause_key_name)
        while True:
            if self.pause:
                pydirectinput.keyUp("e")
                time.sleep(0.1)
                continue

            full_frame = self.capture_screen_full()
            if full_frame is None:
                time.sleep(0.01)
                continue

            if self.new_fish_mini.run(full_frame):
                time.sleep(0.01)
                continue

            region_frame = self.capture_screen()
            if region_frame is None:
                time.sleep(0.01)
                continue

            gray = cv2.cvtColor(region_frame, cv2.COLOR_RGB2GRAY)
            detections = [] if self.went_to_none else self.process_frame_number(gray)

            if detections:
                self._update_number_boxes(detections, region_frame)
                self.went_to_none = False

            if detections or self.went_to_none:
                boxes = self.process_frame_boxes(gray)
            else:
                self._reset_no_detection()
                continue

            if not boxes:
                self._reset_no_detection()
                continue

            action_taken = self._handle_boxes(boxes, region_frame)
            if action_taken:
                self.went_to_none = True
                continue

            now = time.time()
            if now - self.last_no_detection > self.last_no_detection_delay:
                self._click_fail_safe(boxes)
                self.last_no_detection = now


def load_config(path: str = "config.toml") -> Dict[str, Any]:
    try:
        return toml.load(path)
    except FileNotFoundError as exc:
        raise ConfigError("config.toml was not found.") from exc
    except toml.TomlDecodeError as exc:
        raise ConfigError("config.toml contains invalid TOML.") from exc


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    config = load_config()
    auto_fish = FivemAutoFish(config)
    try:
        auto_fish.run()
    except KeyboardInterrupt:
        LOGGER.info("Shutting down at user request.")


if __name__ == "__main__":
    main()

