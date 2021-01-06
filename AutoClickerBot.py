from pyautogui import *
import pyautogui 
import time
import keyboard
import random
import win32api, win32con

## This code is just an autoclicker


try:
    while keyboard.is_pressed('q') == False:
        while keyboard.is_pressed('e') == True:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.001)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
except :
    pass  