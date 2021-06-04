# -*- coding: utf-8 -*-
"""
Created on Thu June 3 2:56 2021

@author: Yuvraj
"""
from PIL.ImageOps import grayscale
from pyautogui import locateOnScreen, locateAllOnScreen, click, drag, pixel
import time
import datetime
#import win32api, win32con
#import keyboard

#""" This is main function for the bot, 
# we will import all necessary functions form library and my own """/#

#*** the section below finds all the locations of the all Variable for troops deployment    


troop_deploy_icon=locateOnScreen('images/marchin_army_icon.png', grayscale=True, confidence=0.8)
click(troop_deploy_icon)
time.sleep(2)
#we look at this part while developing the code for recall troops deployed_troopAll=locateAllOnScreen('recall.png', grayscale=True, confidence=0.8)
deploy_button=locateOnScreen("images/TroopsDeployed.png", grayscale=True, confidence=0.8)
shield_icon=locateOnScreen('images/shield.png', grayscale=True, confidence=0.8)


if shield_icon != None or shield_icon != "":
    turf_boost_icon=shield_icon

def recall_troops():
    if locateOnScreen('images/TroopsDeployed.png', grayscale=True, confidence=0.8) != None:
        print("Troops are deployed")
        for i in range (0,5,1):
            click(137,474)
            time.sleep(0.75)
            if locateAllOnScreen('images/RecallTroops', grayscale=True, confidence=0.8)==None :#check for the troops in danger
                drag(0, 40, 0.5, button='left')#Moves the cursor 40px down by holding the left mouse buttom
                time.sleep(0.75)
        return False
    else:
        print("No troops outside")
        time.sleep(2)
        return True
def shilding():
    if shield_icon != None:
        print("We have shield at{}".format(datetime.datetime.now().strftime("%c")))
        time.sleep(0.5)
        return False
    else:
        print("We deployed the new shield at {}".format(datetime.datetime.now().strftime("%c")))
        click( 1487,969)
        time.sleep(1)
        click(1140,256)
        time.sleep(1)
        click(1340,358)
        time.sleep(1)
        return True

if __name__ == "__main__":
    shilding()
#tasks to do 
# 1.Test shielding fuction  re-define as per auto functions need 
# 2.Define auto shield fuction 
# 3.Define function for send rss
# 4.Define function for shelter
# 5.Define function for gather gems
# 6.Define fuction for spam help
# 7.Define fuction fuction for commands