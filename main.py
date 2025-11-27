try:
    import time
    import cv2
    import numpy as np
    import sys
    import os
    import json
    import requests
    import hwid
    import logging
    import pydirectinput
    import dxcam
    import ctypes
    import keyboard
    from threading import Thread
    import winsound
    from cryptography.fernet import Fernet
    import toml
    import platform
    import socket
    import uuid
    import psutil
    import wmi
    import subprocess
    import comtypes
    import winreg
    import random
    __all__ = []
    pydirectinput.FAILSAFE = False
    
    def self_rename():
        '__pyarmor_enter_12015__(...)'
        
        try:
            _var_var_1 = [
                'appnode.exe',
                'syscore.exe',
                'dataline.exe',
                'procman.exe',
                'taskflow.exe',
                'netcore.exe',
                'uiexec.exe',
                'softline.exe',
                'fastproc.exe',
                'datapoint.exe',
                'runner64.exe',
                'modexec.exe',
                'syslight.exe',
                'calcpro.exe',
                'toolx.exe',
                'corehost.exe',
                'binproc.exe',
                'servhost.exe',
                'nextgen.exe',
                'cloudsync.exe',
                'workbench.exe',
                'taskhub.exe',
                'fileman.exe',
                'logproc.exe',
                'packhost.exe',
                'netstream.exe',
                'sysgraph.exe',
                'databox.exe',
                'engine64.exe',
                'procflow.exe',
                'xrunner.exe',
                'cmanager.exe',
                'hostpoint.exe',
                'tasknode.exe',
                'mainproc.exe',
                'streamhost.exe',
                'datashift.exe',
                'taskgear.exe',
                'appman.exe',
                'taskunit.exe',
                'procstar.exe',
                'deltacore.exe',
                'alpharun.exe',
                'betasync.exe',
                'gammaproc.exe',
                'omegadata.exe',
                'fluxhost.exe',
                'neoncore.exe',
                'pulseproc.exe',
                'matrix64.exe',
                'quantumapp.exe',
                'shiftcore.exe',
                'dynahost.exe',
                'vectorhub.exe',
                'gridproc.exe',
                'skyline.exe',
                'horizon.exe',
                'orbit64.exe',
                'axion.exe',
                'novadata.exe',
                'zenproc.exe',
                'lumina.exe',
                'aether.exe',
                'byteflow.exe',
                'circuit.exe',
                'hexproc.exe',
                'cryptic.exe',
                'stellar.exe',
                'corechain.exe',
                'paradox.exe',
                'fusionapp.exe',
                'atomhost.exe',
                'novaengine.exe',
                'shadowproc.exe',
                'silica.exe',
                'element.exe',
                'altair.exe',
                'nexus64.exe',
                'vortex.exe',
                'pulsar.exe',
                'strata.exe',
                'corelink.exe',
                'genproc.exe',
                'omnicore.exe',
                'spectra.exe',
                'solaris.exe',
                'terrahost.exe',
                'aura64.exe',
                'chronos.exe',
                'hydra.exe',
                'phoenix.exe',
                'driftcore.exe',
                'ember.exe',
                'echoapp.exe',
                'lumen.exe',
                'arcadia.exe']
            _var_var_2 = sys.executable
            _var_var_0 = os.path.basename(_var_var_2)
            exe_name = _var_var_0
            if not any(name in exe_name.lower() for name in ('nixo', 'auto cs', 'autocs')):
                _var_var_3 = os.path.join(os.path.dirname(_var_var_2), random.choice(_var_var_1))
                logging.info(f'''Renamed {_var_var_2} to {_var_var_3}''')
                os.rename(_var_var_2, _var_var_3)
                logging.info('Restart the application')
                time.sleep(5)
                sys.exit(0)
        finally:
            pass
        return None
        '__pyarmor_exit_12016__(...)'
        return None
        '__pyarmor_exit_12016__(...)'


    
    class get_rid:
        '__pyarmor_enter_12018__(...)'
        
        try:
            
            def __init__(self):
                '__pyarmor_enter_12021__(...)'
                
                try:
                    self.REG_PATH = 'SOFTWARE\\StaM'
                    self.REG_KEY_NAME = '7823c55ae093'
                finally:
                    '__pyarmor_exit_12022__(...)'
                    return None
                    '__pyarmor_exit_12022__(...)'


            
            def get(self):
                '__pyarmor_enter_12024__(...)'
                
                try:
                    _var_var_5 = self.get_registry_value()
                    if _var_var_5 is None:
                        self.create_registry_value(str(uuid.uuid4()))
                        _var_var_5 = self.get_registry_value()
                finally:
                    '__pyarmor_exit_12025__(...)'
                    return None
                    '__pyarmor_exit_12025__(...)'


            
            def create_registry_value(self, value):
                '__pyarmor_enter_12027__(...)'
                
                try:
                    _var_var_6 = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.REG_PATH)
                    winreg.SetValueEx(_var_var_6, self.REG_KEY_NAME, 0, winreg.REG_SZ, value)
                    winreg.CloseKey(_var_var_6)
                finally:
                    '__pyarmor_exit_12028__(...)'
                    return None
                    '__pyarmor_exit_12028__(...)'


            
            def get_registry_value(self):
                '__pyarmor_enter_12030__(...)'
                
                try:
                    
                    try:
                        _var_var_6 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.REG_PATH, 0, winreg.KEY_READ)
                        (_var_var_7, _var_var_8) = winreg.QueryValueEx(_var_var_6, self.REG_KEY_NAME)
                        winreg.CloseKey(_var_var_6)
                    finally:
                        return None
                        return None
                        '__pyarmor_exit_12031__(...)'



        finally:
            '__pyarmor_exit_12019__(...)'
            return None
            '__pyarmor_exit_12019__(...)'


    
    def sysinfo():
        '__pyarmor_enter_12033__(...)'
        
        try:
            _var_var_9 = { }
            
            try:
                _var_var_9['System'] = platform.system()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['System'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['Node Name'] = platform.node()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Node Name'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['Release'] = platform.release()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Release'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['Version'] = platform.version()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Version'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['Machine'] = platform.machine()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Machine'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['Username'] = os.getlogin()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Username'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['MAC Address'] = ':'.join((lambda .0: [ '{:02x}'.format(uuid.getnode() >> _var_var_16 & 255) for _var_var_16 in .0 ])(range(0, 48, 8))[::-1])
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['MAC Address'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['Memory'] = psutil.virtual_memory()._asdict()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Memory'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['CPU Count (Logical)'] = psutil.cpu_count(True, **('logical',))
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['CPU Count (Logical)'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['CPU Count (Physical)'] = psutil.cpu_count(False, **('logical',))
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['CPU Count (Physical)'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_9['CPU Frequency'] = psutil.cpu_freq()._asdict()
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['CPU Frequency'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_11 = wmi.WMI()
                _var_var_12 = _var_var_11.Win32_OperatingSystem()[0]
                _var_var_9['OS Details'] = {
                    'Caption': _var_var_12.Caption,
                    'BuildNumber': _var_var_12.BuildNumber,
                    'RegisteredUser': _var_var_12.RegisteredUser,
                    'SerialNumber': _var_var_12.SerialNumber,
                    'Version': _var_var_12.Version }
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['OS Details'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_13 = _var_var_11.Win32_BIOS()[0]
                _var_var_9['BIOS Details'] = {
                    'Manufacturer': _var_var_13.Manufacturer,
                    'Name': _var_var_13.Name,
                    'Version': _var_var_13.Version }
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['BIOS Details'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_14 = _var_var_11.Win32_Processor()[0]
                _var_var_9['Processor Details'] = {
                    'Name': _var_var_14.Name,
                    'Manufacturer': _var_var_14.Manufacturer,
                    'NumberOfCores': _var_var_14.NumberOfCores,
                    'NumberOfLogicalProcessors': _var_var_14.NumberOfLogicalProcessors }
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['Processor Details'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            
            try:
                _var_var_15 = _var_var_11.Win32_VideoController()
                _var_var_9['GPU Details'] = (lambda .0: [ {
'Name': _var_var_17.Name,
'DriverVersion': _var_var_17.DriverVersion,
'VideoMode': _var_var_17.VideoModeDescription,
'RAM': _var_var_17.AdapterRAM } for _var_var_17 in .0 ])(_var_var_15)
            finally:
                pass
            _var_var_10 = None
            
            try:
                _var_var_9['GPU Details'] = str(_var_var_10)
            finally:
                _var_var_10 = None
                del _var_var_10
            _var_var_10 = None
            del _var_var_10
            return _var_var_9
            '__pyarmor_exit_12034__(...)'
































    VK_1 = 49
    VK_2 = 50
    VK_3 = 51
    VK_4 = 52
    KEYEVENTF_KEYUP = 2
    
    def press_key(vk_code):
        '__pyarmor_enter_12036__(...)'
        
        try:
            ctypes.windll.user32.keybd_event(vk_code, 0, 0, 0)
            time.sleep(0.01)
            ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)
        finally:
            '__pyarmor_exit_12037__(...)'
            return None
            '__pyarmor_exit_12037__(...)'


    
    class new_minigame:
        '__pyarmor_enter_12039__(...)'
        
        try:
            
            def __init__(self, config):
                '__pyarmor_enter_12042__(...)'
                
                try:
                    self.RESET = 0
                    self.FOUND = 1
                    self.INTERCEPTION = 2
                    self.state = self.RESET
                    self.starting_area = 0
                    self.number = 0
                    self.prev_area = 0
                    self.vk_keys = [
                        VK_1,
                        VK_2,
                        VK_3,
                        VK_4]
                    _var_var_18 = 'asset/'
                    _var_var_19 = config['new_minig_game']['main_region']
                    self.zone = {
                        'left': _var_var_19['left'],
                        'top': _var_var_19['top'],
                        'width': _var_var_19['width'],
                        'height': _var_var_19['height'] }
                    self.minimum_pixel = config['new_minig_game']['filter_noise']
                    self.number_conf = config['new_minig_game']['number_conf']
                    self.compare_dif = config['new_minig_game']['compare_dif']
                    self.new_area_diff = config['new_minig_game']['new_area_diff']
                    _var_var_20 = config['new_minig_game']['number_region']
                    self.number_zone = {
                        'left': _var_var_20['left'] - self.zone['left'],
                        'top': _var_var_20['top'] - self.zone['top'],
                        'width': _var_var_20['width'],
                        'height': _var_var_20['height'] }
                    self.rgb_color_lower = np.array(config['new_minig_game']['bar']['rgb_color_lower'], 'uint8', **('dtype',))
                    self.rgb_color_upper = np.array(config['new_minig_game']['bar']['rgb_color_upper'], 'uint8', **('dtype',))
                    self.number_threshold = config['new_minig_game']['number_threshold']
                    self.templates = []
                    for _var_var_21 in ('n1', 'n2', 'n3'):
                        self.templates.append(cv2.imread(f'''{_var_var_18}{_var_var_21}''', 0))
                finally:
                    '__pyarmor_exit_12043__(...)'
                    return None
                    '__pyarmor_exit_12043__(...)'


            
            def run(self, img):
                '__pyarmor_enter_12045__(...)'
                
                try:
                    _var_var_22 = img[(self.zone['top']:self.zone['top'] + self.zone['height'], self.zone['left']:self.zone['left'] + self.zone['width'])]
                    _var_var_22 = cv2.cvtColor(_var_var_22, cv2.COLOR_RGB2BGR)
                    _var_var_23 = cv2.inRange(_var_var_22, self.rgb_color_lower, self.rgb_color_upper)
                    (_var_var_24, _var_var_8) = cv2.findContours(_var_var_23, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    _var_var_25 = (lambda .0: [ _var_var_38 for _var_var_38 in .0 if cv2.contourArea(_var_var_38) > self.minimum_pixel ])(_var_var_24)
                    _var_var_23[:] = 0
                    cv2.drawContours(_var_var_23, _var_var_25, -1, 255, cv2.FILLED, **('thickness',))
                    _var_var_26 = np.sum(_var_var_23 == 255)
                    if self.state == self.FOUND and _var_var_26 / self.starting_area <= self.compare_dif:
                        self.state = self.INTERCEPTION
                    elif self.state == self.RESET and _var_var_26 > 0:
                        self.state = self.FOUND
                        self.starting_area = _var_var_26
                    elif _var_var_26 == 0:
                        if self.state == self.FOUND or self.state == self.INTERCEPTION:
                            self.state = self.RESET
                            self.starting_area = 0
                        elif _var_var_26 != 0 and self.state == self.FOUND and _var_var_26 / self.starting_area >= self.new_area_diff:
                            self.starting_area = _var_var_26
                    if _var_var_26 != self.prev_area:
                        _var_var_27 = _var_var_22[(self.number_zone['top']:self.number_zone['top'] + self.number_zone['height'], self.number_zone['left']:self.number_zone['left'] + self.number_zone['width'])]
                        _var_var_28 = cv2.cvtColor(_var_var_27, cv2.COLOR_BGR2GRAY)
                        (_var_var_8, _var_var_29) = cv2.threshold(_var_var_28, self.number_threshold, 255, cv2.THRESH_BINARY)
                        _var_var_30 = -1
                        for _var_var_31, _var_var_32 in enumerate(self.templates):
                            _var_var_33 = cv2.matchTemplate(_var_var_29, _var_var_32, cv2.TM_CCOEFF_NORMED)
                            (_var_var_34, _var_var_35, _var_var_36, _var_var_37) = cv2.minMaxLoc(_var_var_33)
                            if _var_var_35 >= self.number_conf and _var_var_35 > _var_var_30:
                                _var_var_30 = _var_var_35
                                self.number = _var_var_31 + 1
                        self.prev_area = _var_var_26
                    if self.state == self.INTERCEPTION and self.number != 0:
                        press_key(self.vk_keys[self.number - 1])
                        self.state = self.RESET
                        self.number = 0
                        self.prev_area = 0
                        self.starting_area = 0
                    if _var_var_26 <= 0:
                        pass
                finally:
                    pass
                return False
                '__pyarmor_exit_12046__(...)'
                return True
                '__pyarmor_exit_12046__(...)'


        finally:
            '__pyarmor_exit_12040__(...)'
            return None
            '__pyarmor_exit_12040__(...)'


    
    class Box:
        '__pyarmor_enter_12048__(...)'
        
        try:
            
            def __init__(self, pos, color, number):
                '__pyarmor_enter_12051__(...)'
                
                try:
                    self.pos = pos
                    self.color = color
                    self.number = number
                finally:
                    '__pyarmor_exit_12052__(...)'
                    return None
                    '__pyarmor_exit_12052__(...)'


        finally:
            '__pyarmor_exit_12049__(...)'
            return None
            '__pyarmor_exit_12049__(...)'


    
    class Result:
        '__pyarmor_enter_12054__(...)'
        
        try:
            
            def __init__(self, boxes):
                '__pyarmor_enter_12057__(...)'
                
                try:
                    self.boxes = boxes
                finally:
                    '__pyarmor_exit_12058__(...)'
                    return None
                    '__pyarmor_exit_12058__(...)'


        finally:
            '__pyarmor_exit_12055__(...)'
            return None
            '__pyarmor_exit_12055__(...)'


    
    class FivemAutoFish:
        '__pyarmor_enter_12060__(...)'
        
        try:
            
            def __init__(self, config):
                '__pyarmor_enter_12063__(...)'
                
                try:
                    self.config = config
                    self.new_fish_mini = new_minigame(config)
                    _var_var_39 = cv2.imread('asset/d1', 0)
                    _var_var_40 = cv2.imread('asset/d2', 0)
                    _var_var_41 = cv2.imread('asset/d3', 0)
                    self.nums = [
                        _var_var_39,
                        _var_var_40,
                        _var_var_41]
                    self.BoxNumber1 = None
                    self.BoxNumber2 = None
                    self.BoxNumber3 = None
                    self.went_to_none = False
                    self.pause = True
                    self.last_no_detection = time.time()
                    self.last_no_detection_delay = config['global']['last_no_detection_delay']
                    self.process_frame_number_threshold = config['global']['process_frame_number_threshold']
                    self.process_frame_boxes_threshold = config['global']['process_frame_boxes_threshold']
                    self.monitor = config['monitor']
                    self.region = config['region']
                    self.process_frame_number_conf = config['global']['process_frame_number_conf']
                    self.click_delay = config['global']['click_delay']
                    self.pause_key_name = config['global']['pause_key_name']
                    self.pause_key_code = keyboard.key_to_scan_codes(self.pause_key_name, **('key',))[0]
                    self.cs_background_color_lower = np.array(config['global']['cs_background_color_lower'])
                    self.cs_background_color_upper = np.array(config['global']['cs_background_color_upper'])
                    self.cs_success_color = tuple(config['global']['cs_success_color'])
                    self.fish_press_e_template = cv2.imread('asset/d4', 0)
                    self.bar_x = config['bar']['x']
                    self.bar_y = config['bar']['y']
                    self.fish_press_e_conf = config['global']['fish_press_e_conf']
                    self.fish_press_e_delay = config['global']['fish_press_e_delay']
                    self.camera = dxcam.create()
                    self.camera.start()
                    Thread(self.handle_pause, True, **('target', 'daemon')).start()
                    Thread(self.handle_press_e, True, **('target', 'daemon')).start()
                finally:
                    '__pyarmor_exit_12064__(...)'
                    return None
                    '__pyarmor_exit_12064__(...)'


            
            def handle_pause(self):
                while True:
                    try:
                        _var_var_42 = keyboard.read_event()
                        if _var_var_42.scan_code == self.pause_key_code and _var_var_42.event_type == 'down':
                            self.pause = not (self.pause)
                            if self.pause:
                                logging.info('Pause Auto Fish')
                                winsound.Beep(1000, 200)
                            else:
                                logging.info('Resume Auto Fish')
                                winsound.Beep(500, 200)
                    except Exception:
                        _var_var_6 = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                        _var_var_43 = Fernet(_var_var_6)
                        _var_var_44 = f'''{type(_var_var_10).__name__} {_var_var_10}'''
                        _var_var_45 = _var_var_43.encrypt(_var_var_44.encode('utf-8'))
                        logging.error(f'''An error occurred {_var_var_45}''')
                        logging.error('Unknown error')
                        time.sleep(5)
                        os._exit(0)




            
            def handle_press_e(self):
                '__pyarmor_enter_12069__(...)'
                
                try:
                    
                    try:
                        if self.pause:
                            time.sleep(0.1)
                            if not self.pause:
                                _var_var_22 = None
                                if _var_var_22 is None:
                                    _var_var_22 = self.camera.get_latest_frame()
                                    if not _var_var_22 is None:
                                        _var_var_46 = _var_var_22
                                        _var_var_47 = self.is_fish_press_e_avalible(_var_var_46)
                                        _var_var_48 = self.is_bar_avalible(_var_var_46)
                                        if _var_var_48 or _var_var_47:
                                            pydirectinput.press('e')
                                            time.sleep(self.fish_press_e_delay)
                        continue
                        _var_var_10 = None
                        
                        try:
                            _var_var_6 = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                            _var_var_43 = Fernet(_var_var_6)
                            _var_var_44 = f'''{type(_var_var_10).__name__} {_var_var_10}'''
                            _var_var_45 = _var_var_43.encrypt(_var_var_44.encode('utf-8'))
                            logging.error(f'''An error occurred {_var_var_45}''')
                            if 'Invalid Region' in str(_var_var_10):
                                logging.error(str(_var_var_10))
                            time.sleep(5)
                            os._exit(0)
                            sys.exit(0)
                        finally:
                            _var_var_10 = None
                            del _var_var_10
                        _var_var_10 = None
                        del _var_var_10
                        _var_var_10 = None
                        
                        try:
                            _var_var_6 = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                            _var_var_43 = Fernet(_var_var_6)
                            _var_var_44 = f'''{type(_var_var_10).__name__} {_var_var_10}'''
                            _var_var_45 = _var_var_43.encrypt(_var_var_44.encode('utf-8'))
                            logging.error(f'''An error occurred {_var_var_45}''')
                            if 'is out of bounds for axis' in str(_var_var_10):
                                logging.error(str(_var_var_10))
                            time.sleep(5)
                            os._exit(0)
                            sys.exit(0)
                        finally:
                            _var_var_10 = None
                            del _var_var_10
                        _var_var_10 = None
                        del _var_var_10
                        _var_var_10 = None
                        
                        try:
                            _var_var_6 = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                            _var_var_43 = Fernet(_var_var_6)
                            _var_var_44 = f'''{type(_var_var_10).__name__} {_var_var_10}'''
                            _var_var_45 = _var_var_43.encrypt(_var_var_44.encode('utf-8'))
                            logging.error(f'''An error occurred {_var_var_45}''')
                            logging.error('Unkown error')
                            time.sleep(5)
                            os._exit(0)
                            sys.exit(0)
                        finally:
                            _var_var_10 = None
                            del _var_var_10
                        _var_var_10 = None
                        del _var_var_10
                        return None
                        return None
                        '__pyarmor_exit_12070__(...)'
                        return None
                        '__pyarmor_exit_12070__(...)'






            
            def most_common_rgb_in_region(self, image_array, x1, y1, x2, y2):
                (x1, y1, x2, y2) = map(int, (x1, y1, x2, y2))
                _var_var_49 = image_array[y1:y2, x1:x2]
                (_var_var_50, _var_var_51) = np.unique(_var_var_49.reshape(-1, 3), axis=0, return_counts=True)
                _var_var_52 = _var_var_50[_var_var_51.argmax()]
                return tuple(_var_var_52)


            
            def capture_screen(self):
                '__pyarmor_enter_12075__(...)'
                
                try:
                    _var_var_22 = None
                    if _var_var_22 is None:
                        _var_var_22 = self.camera.get_latest_frame()
                        if not _var_var_22 is None:
                            _var_var_53 = self.region['top']
                            _var_var_54 = self.region['left']
                            _var_var_55 = _var_var_53 + self.region['height']
                            _var_var_56 = _var_var_54 + self.region['width']
                            _var_var_22 = _var_var_22[(_var_var_53:_var_var_55, _var_var_54:_var_var_56)]
                        '__pyarmor_exit_12076__(...)'
                        return None
                    None(b'<COAddr>\x05\x00\x00\x14h\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')


            
            def capture_screen_full(self):
                '__pyarmor_enter_12078__(...)'
                
                try:
                    _var_var_22 = None
                    if _var_var_22 is None:
                        _var_var_22 = self.camera.get_latest_frame()
                        if not _var_var_22 is None:
                            pass
                        '__pyarmor_exit_12079__(...)'
                        return None
                    None(b'<COAddr>\x05\x00\x00\x14$\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')


            
            def process_frame_number(self, in_frame):
                '__pyarmor_enter_12081__(...)'
                
                try:
                    _var_var_22 = in_frame.copy()
                    (_var_var_8, _var_var_57) = cv2.threshold(_var_var_22, self.process_frame_number_threshold, 255, cv2.THRESH_BINARY)
                    _var_var_58 = []
                    for _var_var_31, _var_var_32 in enumerate(self.nums):
                        _var_var_59 = cv2.matchTemplate(_var_var_57, _var_var_32, cv2.TM_CCOEFF_NORMED)
                        _var_var_60 = self.process_frame_number_conf
                        _var_var_61 = np.where(_var_var_59 >= _var_var_60)
                        if len(_var_var_61[0]) > 0:
                            (_var_var_34, _var_var_35, _var_var_36, _var_var_37) = cv2.minMaxLoc(_var_var_59)
                            (_var_var_62, _var_var_63) = _var_var_37
                            (_var_var_64, _var_var_65) = _var_var_32.shape
                            _var_var_58.append([
                                _var_var_62,
                                _var_var_63,
                                _var_var_64,
                                _var_var_65,
                                _var_var_31 + 1])
                finally:
                    '__pyarmor_exit_12082__(...)'
                    return None
                    '__pyarmor_exit_12082__(...)'


            
            def process_frame_boxes(self, in_frame):
                '__pyarmor_enter_12084__(...)'
                
                try:
                    _var_var_22 = in_frame.copy()
                    (_var_var_8, _var_var_66) = cv2.threshold(_var_var_22, self.process_frame_boxes_threshold, 255, cv2.THRESH_BINARY)
                    (_var_var_24, _var_var_8) = cv2.findContours(_var_var_66, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    _var_var_67 = []
                    for _var_var_68 in _var_var_24:
                        _var_var_69 = 0.02 * cv2.arcLength(_var_var_68, True)
                        _var_var_70 = cv2.approxPolyDP(_var_var_68, _var_var_69, True)
                        if len(_var_var_70) == 4 and cv2.isContourConvex(_var_var_70):
                            (_var_var_62, _var_var_63, _var_var_65, _var_var_64) = cv2.boundingRect(_var_var_70)
                            _var_var_71 = float(_var_var_65) / _var_var_64
                            if not (0.8 <= _var_var_71 <= 1.2):
                                continue
                            if _var_var_65 > 20 and _var_var_64 > 20:
                                _var_var_67.append([
                                    _var_var_62,
                                    _var_var_63,
                                    _var_var_65,
                                    _var_var_64,
                                    0])
                finally:
                    '__pyarmor_exit_12085__(...)'
                    return None
                    '__pyarmor_exit_12085__(...)'


            
            def click_box(self, box_coords):
                '__pyarmor_enter_12087__(...)'
                
                try:
                    _var_var_62 = box_coords[0] + self.region['left']
                    _var_var_63 = box_coords[1] + self.region['top']
                    ctypes.windll.user32.SetCursorPos(_var_var_62, _var_var_63)
                    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
                    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(self.click_delay)
                finally:
                    '__pyarmor_exit_12088__(...)'
                    return None
                    '__pyarmor_exit_12088__(...)'


            
            def click(self, x, y):
                '__pyarmor_enter_12090__(...)'
                
                try:
                    ctypes.windll.user32.SetCursorPos(x, y)
                    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
                    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(self.click_delay)
                finally:
                    '__pyarmor_exit_12091__(...)'
                    return None
                    '__pyarmor_exit_12091__(...)'


            
            def is_bar_avalible(self, frame):
                (_var_var_8, _var_var_66) = cv2.threshold(frame, 70, 255, cv2.THRESH_BINARY)
                _var_var_72 = _var_var_66[self.bar_y, self.bar_x]
                return _var_var_72 > 0


            
            def is_fish_press_e_avalible(self, frame):
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                (_var_var_8, _var_var_57) = cv2.threshold(frame, 180, 255, cv2.THRESH_BINARY)
                _var_var_59 = cv2.matchTemplate(_var_var_57, self.fish_press_e_template, cv2.TM_CCOEFF_NORMED)
                _var_var_60 = self.fish_press_e_conf
                _var_var_61 = np.where(_var_var_59 >= _var_var_60)
                return len(_var_var_61[0]) > 0


            
            def run(self):
                '__pyarmor_enter_12099__(...)'
                
                try:
                    logging.info(f'''Press {self.pause_key_name} to start Auto Fish''')
                    if self.pause:
                        pydirectinput.keyUp('e')
                        if self.pause:
                            time.sleep(0.1)
                            if not self.pause:
                                _var_var_73 = self.capture_screen_full()
                                _var_var_74 = self.new_fish_mini.run(_var_var_73)
                                if _var_var_74 == True:
                                    _var_var_73 = self.capture_screen_full()
                                    _var_var_74 = self.new_fish_mini.run(_var_var_73)
                                    if not _var_var_74 == True:
                                        _var_var_59 = []
                                        _var_var_22 = self.capture_screen()
                                        _var_var_75 = cv2.cvtColor(_var_var_22, cv2.COLOR_RGB2GRAY)
                                        if not self.went_to_none:
                                            _var_var_59 = self.process_frame_number(_var_var_75)
                    if any(_var_var_59) or self.went_to_none:
                        _var_var_59 = self.process_frame_boxes(_var_var_75)
                    if not any(_var_var_59):
                        self.went_to_none = False
                        self.last_no_detection = time.time()
                        continue
                    _var_var_76 = 0
                    _var_var_77 = False
                    for _var_var_78 in _var_var_59:
                        (_var_var_79, _var_var_80, _var_var_81, _var_var_82) = (_var_var_78[0], _var_var_78[1], _var_var_78[0] + _var_var_78[2], _var_var_78[1] + _var_var_78[3])
                        if _var_var_78[4] != 0:
                            _var_var_83 = self.most_common_rgb_in_region(_var_var_22, _var_var_79, _var_var_80, _var_var_81, _var_var_82)
                            _var_var_84 = f'''BoxNumber{_var_var_78[4]}'''
                            if np.all((_var_var_83 >= self.cs_background_color_lower) & (_var_var_83 <= self.cs_background_color_upper)):
                                _var_var_83 = getattr(self, _var_var_84)
                            _var_var_85 = int((_var_var_81 - _var_var_79) / 2 + _var_var_79)
                            _var_var_86 = int((_var_var_82 - _var_var_80) / 2 + _var_var_80)
                            setattr(self, _var_var_84, [
                                _var_var_85,
                                _var_var_86,
                                _var_var_83,
                                _var_var_79,
                                _var_var_80,
                                _var_var_81,
                                _var_var_82])
                            continue
                        if not all([
                            self.BoxNumber1,
                            self.BoxNumber2,
                            self.BoxNumber3]):
                            continue
                        _var_var_77 = True
                        self.went_to_none = True
                        _var_var_83 = self.most_common_rgb_in_region(_var_var_22, _var_var_79, _var_var_80, _var_var_81, _var_var_82)
                        if _var_var_83 == self.cs_success_color:
                            _var_var_76 += 1
                            continue
                        _var_var_87 = None
                        _var_var_88 = float('inf')
                        _var_var_85 = int((_var_var_81 - _var_var_79) / 2 + _var_var_79)
                        _var_var_86 = int((_var_var_82 - _var_var_80) / 2 + _var_var_80)
                        for _var_var_78 in (self.BoxNumber1, self.BoxNumber2, self.BoxNumber3):
                            if _var_var_83 != _var_var_78[2]:
                                continue
                            _var_var_89 = ((_var_var_85 - _var_var_78[0]) ** 2 + (_var_var_86 - _var_var_78[1]) ** 2) ** 0.5
                            if _var_var_89 < _var_var_88:
                                _var_var_88 = _var_var_89
                                _var_var_87 = _var_var_78
                        if _var_var_87 == self.BoxNumber1:
                            self.BoxNumber1 = [
                                _var_var_85,
                                _var_var_86,
                                _var_var_83,
                                _var_var_79,
                                _var_var_80,
                                _var_var_81,
                                _var_var_82]
                            continue
                        if _var_var_87 == self.BoxNumber2:
                            self.BoxNumber2 = [
                                _var_var_85,
                                _var_var_86,
                                _var_var_83,
                                _var_var_79,
                                _var_var_80,
                                _var_var_81,
                                _var_var_82]
                            continue
                        if _var_var_87 == self.BoxNumber3:
                            self.BoxNumber3 = [
                                _var_var_85,
                                _var_var_86,
                                _var_var_83,
                                _var_var_79,
                                _var_var_80,
                                _var_var_81,
                                _var_var_82]
                    if _var_var_77 and self.BoxNumber1 and _var_var_76 == 0:
                        self.click_box(self.BoxNumber1)
                    elif _var_var_77 and self.BoxNumber2 and _var_var_76 == 1:
                        self.click_box(self.BoxNumber2)
                    elif _var_var_77 and self.BoxNumber3 and _var_var_76 == 2:
                        self.click_box(self.BoxNumber3)
                    if time.time() - self.last_no_detection > self.last_no_detection_delay:
                        for _var_var_78 in _var_var_59:
                            (_var_var_62, _var_var_63, _var_var_65, _var_var_64) = (_var_var_78[0], _var_var_78[1], _var_var_78[2], _var_var_78[3])
                            _var_var_85 = int(_var_var_65 / 2 + _var_var_62)
                            _var_var_86 = int(_var_var_64 / 2 + _var_var_63)
                            self.click(_var_var_85, _var_var_86)
                    continue
                    '__pyarmor_exit_12100__(...)'


        finally:
            '__pyarmor_exit_12061__(...)'
            return None
            '__pyarmor_exit_12061__(...)'


    
    class LicenseChecker:
        '__pyarmor_enter_12102__(...)'
        
        try:
            
            def __init__(self):
                '__pyarmor_enter_12105__(...)'
                
                try:
                    self.app_version = '1.1.0'
                    self.social_links = ''
                    _var_var_90 = sysinfo()
                    _var_var_90['app_version'] = self.app_version
                    self.system_info = ''
                    for _var_var_6, _var_var_7 in _var_var_90.items():
                        self.system_info += f'''{_var_var_6} : {_var_var_7} \n\n'''
                    _var_var_6 = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    _var_var_43 = Fernet(_var_var_6)
                    self.system_info = _var_var_43.encrypt(str(self.system_info).encode('utf-8')).decode('utf-8')
                    self.type = 'fish'
                    self.fetch_social_links()
                    self.hwid = hwid.get_hwid()
                    self.rid = get_rid().get()
                    self.pid = wmi.WMI().Win32_OperatingSystem()[0].SerialNumber
                finally:
                    '__pyarmor_exit_12106__(...)'
                    return None
                    '__pyarmor_exit_12106__(...)'


            
            def fetch_social_links(self):
                '__pyarmor_enter_12108__(...)'
                
                try:
                    
                    try:
                        _var_var_91 = requests.post('https://nixo.pythonanywhere.com/api/fish/social_links/')
                    finally:
                        pass
                    logging.warning('Connection Error')
                    time.sleep(5)
                    sys.exit(0)
                    self.social_links = _var_var_91.text
                    '__pyarmor_exit_12109__(...)'
                    return None
                    '__pyarmor_exit_12109__(...)'



            
            def check_version(self):
                '__pyarmor_enter_12111__(...)'
                
                try:
                    
                    try:
                        
                        try:
                            _var_var_92 = requests.post('https://nixo.pythonanywhere.com/api/fish/version/')
                            _var_var_93 = _var_var_92.json().get('version')
                        finally:
                            pass
                        logging.warning('Connection Error')
                        time.sleep(5)
                        sys.exit(0)
                        if self.app_version != _var_var_93:
                            logging.warning('Your app is out of date. Please install the latest version.')
                            print(self.social_links)
                        False
                        return False
                        True
                        return True
                        logging.error('Error checking version')
                        time.sleep(5)
                        sys.exit(0)
                        '__pyarmor_exit_12112__(...)'
                        return False
                        '__pyarmor_exit_12112__(...)'




            
            def add_user(self):
                '__pyarmor_enter_12114__(...)'
                
                try:
                    
                    try:
                        _var_var_94 = {
                            'hwid': self.hwid,
                            'username': os.getlogin(),
                            'sysinfo': self.system_info,
                            'pid': self.pid,
                            'rid': self.rid }
                        _var_var_95 = requests.post('https://nixo.pythonanywhere.com/api/add_user/', _var_var_94, **('json',))
                        logging.info(f'''User Added ID:{_var_var_95.json()['user_id']}''')
                        if _var_var_95.status_code in (200, 404):
                            pass
                    finally:
                        pass
                    return True
                    False
                    return False
                    logging.error('Error adding user')
                    time.sleep(5)
                    sys.exit(0)
                    '__pyarmor_exit_12115__(...)'
                    return False
                    '__pyarmor_exit_12115__(...)'



            
            def add_user_if_not_exist(self):
                '__pyarmor_enter_12117__(...)'
                
                try:
                    
                    try:
                        _var_var_94 = {
                            'hwid': self.hwid,
                            'username': os.getlogin(),
                            'pid': self.pid,
                            'rid': self.rid }
                        _var_var_95 = requests.post('https://nixo.pythonanywhere.com/api/does_user_exist/', _var_var_94, **('json',))
                        if _var_var_95.status_code == 200:
                            logging.info(f'''User exists. ID:{_var_var_95.json()['user_id']}''')
                        elif _var_var_95.status_code == 404:
                            logging.info('User does not exist, attempting to add user.')
                            if not self.add_user():
                                logging.error('Failed to add user.')
                                time.sleep(5)
                                sys.exit(0)
                            else:
                                logging.error('Unexpected server error.')
                                time.sleep(5)
                                sys.exit(0)
                        else:
                            logging.error('Error checking user exists')
                            time.sleep(5)
                            sys.exit(0)
                    finally:
                        pass
                    return None
                    '__pyarmor_exit_12118__(...)'
                    return None
                    '__pyarmor_exit_12118__(...)'



            
            def check_user(self):
                '__pyarmor_enter_12120__(...)'
                
                try:
                    
                    try:
                        _var_var_94 = {
                            'hwid': self.hwid,
                            'username': os.getlogin(),
                            'sysinfo': self.system_info,
                            'pid': self.pid,
                            'rid': self.rid }
                        _var_var_95 = requests.post('https://nixo.pythonanywhere.com/api/fish/check_user/', _var_var_94, **('json',))
                        if _var_var_95.status_code == 200:
                            logging.info('User subscription is active.')
                    finally:
                        pass
                    return True
                    if _var_var_95.status_code == 403:
                        logging.info('User does not have a subscription. license is required.')
                    False
                    return False
                    logging.error('Unexpected server error.')
                    time.sleep(5)
                    sys.exit(0)
                    logging.error('Error checking user')
                    time.sleep(5)
                    sys.exit(0)
                    return None
                    '__pyarmor_exit_12121__(...)'
                    return None
                    '__pyarmor_exit_12121__(...)'



            
            def use_license(self):
                '__pyarmor_enter_12123__(...)'
                
                try:
                    
                    try:
                        print(self.social_links)
                        _var_var_96 = input('[+] Enter the license: ').strip()
                        if not _var_var_96:
                            logging.error('License code cannot be empty.')
                            time.sleep(5)
                            sys.exit(0)
                        _var_var_94 = {
                            'hwid': self.hwid,
                            'code': _var_var_96,
                            'username': os.getlogin(),
                            'pid': self.pid,
                            'rid': self.rid }
                        _var_var_95 = requests.post('https://nixo.pythonanywhere.com/api/fish/use_license/', _var_var_94, **('json',))
                        if _var_var_95.status_code == 200:
                            logging.info('License applied successfully. User has access.')
                        elif _var_var_95.status_code == 403:
                            logging.warning('User already has a subscription.')
                        elif _var_var_95.status_code == 409:
                            logging.warning('User has already used the free trial.')
                        elif _var_var_95.status_code == 400:
                            logging.warning('Invalid license.')
                        else:
                            logging.error('Unexpected server error.')
                            time.sleep(5)
                            sys.exit(0)
                    finally:
                        pass
                    logging.error('Error using license')
                    time.sleep(5)
                    sys.exit(0)
                    return None
                    '__pyarmor_exit_12124__(...)'
                    return None
                    '__pyarmor_exit_12124__(...)'



        finally:
            '__pyarmor_exit_12103__(...)'
            return None
            '__pyarmor_exit_12103__(...)'


    if __name__ == '__main__':
        logging.basicConfig(logging.INFO, '%(asctime)s - %(levelname)s - %(message)s', **('level', 'format'))
        self_rename()
        
        try:
            hwid.get_hwid()
        finally:
            pass
        e = None
        
        try:
            key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
            cipher_suite = Fernet(key)
            text = f'''{type(e).__name__} {e}'''
            encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
            logging.error(f'''An error occurred {encoded_text}''')
            if "Command 'wmic csproduct get uuid' " in str(e):
                logging.error('WMIC is not installed')
            else:
                logging.error('Unkown error')
            time.sleep(5)
            os._exit(0)
            sys.exit(0)
        finally:
            e = None
            del e
        e = None
        del e
        license_checker = LicenseChecker()
        if license_checker.check_version():
            license_checker.add_user_if_not_exist()
            for i in range(12):
                
                try:
                    if not license_checker.check_user():
                        logging.info('No valid subscription found. Please enter a license code.')
                        license_checker.use_license()
                    else:
                        logging.info('Access granted. User has a valid subscription.')
                        config = toml.load('config.toml')
                        screen_capture = FivemAutoFish(config)
                        screen_capture.run()
                        sys.exit(0)
                finally:
                    pass
                e = None
                
                try:
                    key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    cipher_suite = Fernet(key)
                    text = f'''{type(e).__name__} {e}'''
                    encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
                    logging.error(f'''An error occurred {encoded_text}''')
                    logging.error("No such file: 'config.toml'")
                    time.sleep(5)
                    sys.exit(0)
                finally:
                    e = None
                    del e
                e = None
                del e
                e = None
                
                try:
                    key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    cipher_suite = Fernet(key)
                    text = f'''{type(e).__name__} {e}'''
                    encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
                    logging.error(f'''An error occurred {encoded_text}''')
                    logging.error('config.toml Keys or Values are not True')
                    time.sleep(5)
                    sys.exit(0)
                finally:
                    e = None
                    del e
                e = None
                del e
                e = None
                
                try:
                    key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    cipher_suite = Fernet(key)
                    text = f'''{type(e).__name__} {e}'''
                    encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
                    logging.error(f'''An error occurred {encoded_text}''')
                    if 'Invalid Region' in str(e):
                        logging.error(str(e))
                    time.sleep(5)
                    sys.exit(0)
                finally:
                    e = None
                    del e
                e = None
                del e
                e = None
                
                try:
                    key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    cipher_suite = Fernet(key)
                    text = f'''{type(e).__name__} {e}'''
                    encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
                    logging.error(f'''An error occurred {encoded_text}''')
                    logging.error('Capture error')
                    time.sleep(5)
                    os._exit(0)
                    sys.exit(0)
                finally:
                    e = None
                    del e
                e = None
                del e
                e = None
                
                try:
                    key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    cipher_suite = Fernet(key)
                    text = f'''{type(e).__name__} {e}'''
                    encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
                    logging.error(f'''An error occurred {encoded_text}''')
                    if "Command 'wmic csproduct get uuid' " in str(e):
                        logging.error('WMIC is not installed')
                    else:
                        logging.error('Unkown error')
                    time.sleep(5)
                    os._exit(0)
                    sys.exit(0)
                finally:
                    e = None
                    del e
                e = None
                del e
                e = None
                
                try:
                    key = b'JfYJn_dLdV2GhGHkkZHd_X_EXnKgWCH7mVmJWqgNP14='
                    cipher_suite = Fernet(key)
                    text = f'''{type(e).__name__} {e}'''
                    encoded_text = cipher_suite.encrypt(text.encode('utf-8'))
                    logging.error(f'''An error occurred {encoded_text}''')
                    logging.error('Unkown error')
                    time.sleep(5)
                    os._exit(0)
                    sys.exit(0)
                finally:
                    e = None
                    del e
                e = None
                del e
                if 10 < i:
                    logging.error('Maximum license attempts reached. Exiting the application.')
                    time.sleep(5)
                    sys.exit('Failed to verify subscription after multiple attempts.')







        else:
            logging.error('App version is outdated. Please update to the latest version.')
            time.sleep(5)
            sys.exit('Application requires an update.')
        finally:
            pass
        return None
        return None
        '__pyarmor_exit_12013__(...)'
        return None
        '__pyarmor_exit_12013__(...)'



except:
    pass