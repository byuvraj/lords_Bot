# -*- coding: utf-8 -*-
"""
Created on Thu June 3 2:56 2021

@author: Yuvraj
"""
from pyautogui import locateAllOnScreen, locateOnScreen, click, drag
from time import sleep
def recall_troops():
    if locateOnScreen('images/TroopsDeployed.png', grayscale=True, confidence=0.55) != None:
        print("Troops are deployed")
        for i in range (0,5,1):
            click(137,474)
            sleep(0.75)
            if locateAllOnScreen('images/RecallTroops', grayscale=True, confidence=0.55)==None :#check for the troops in danger
                drag(0, 40, 0.5, button='left')#Moves the cursor 40px down by holding the left mouse buttom
                sleep(0.75)
        return False
    else:
        print("No troops outside")
        sleep(2)
        return True
