import pyautogui
import time 
while True:
    if pyautogui.locateOnScreen('smile.png', confidence=0.3) == None:
        print("I can not see it")
    else:
        print("I am able to see it")