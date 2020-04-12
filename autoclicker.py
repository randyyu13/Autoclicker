import win32api
import time
from pynput.mouse import Button, Controller
from random import random

print("press Ctrl-C to quit")
print("use P key to toggle autoclicker")
print("hold the scroll wheel button down to use autoclicker")

state_left = win32api.GetAsyncKeyState(0x04)
mouse = Controller()
state_toggle = win32api.GetAsyncKeyState(0x50)
toggle = -1

while True:
    
    leftTemp = win32api.GetAsyncKeyState(0x04)
    # print("left Temp", leftTemp)
    if leftTemp != state_left:
        state_left = leftTemp
    
    toggleTemp = win32api.GetAsyncKeyState(0x50)
    # print(toggleTemp)
    if toggleTemp != state_toggle:
        state_toggle = toggleTemp
        if toggleTemp >= 0:
            state_toggle = toggleTemp
            toggle *= -1
            print("Autoclicker toggled", toggle)

    # print("toggle", toggle)


    if leftTemp < 0:
        if toggle > 0:
            # print("active")
            mouse.click(Button.left)
            negMul = 1
            if random() > 0.5:
                negMul *= -1
            sleepTime = 0.100 + (negMul * random() * 0.03)
            # print(sleepTime)
            time.sleep(sleepTime)

    time.sleep(0.001)