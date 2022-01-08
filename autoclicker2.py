from ctypes import windll, wintypes, byref
from autoclicker import doubleclick
import win32api, win32con
import time
import random

def get_cursor_location():
    cursor = wintypes.POINT()
    windll.user32.GetCursorPos(byref(cursor))
    return cursor.x, cursor.y

def left_click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

def right_click(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y)

def seconds_to_wait(min, max):
    random_float = random.uniform(min, max)
    time.sleep(random_float)

def double_click(type,x,y):
    if type == "left":
        left_click(x,y)
        seconds_to_wait(0.13, 0.2)
        left_click(x,y)
    
    else:
        right_click(x,y)
        seconds_to_wait(0.13, 0.2)
        right_click(x,y)

def main():
    x,y = get_cursor_location()
    double_click("left", x, y)
    

if __name__ == "__main__":
    n = 0 
    while n < 100:
        main()
        print(n)
        n += 1
        
