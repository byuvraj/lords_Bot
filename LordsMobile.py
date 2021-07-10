# -*- coding: utf-8 -*-
"""
Created on Thu June 3 2:56 2021

@author: Yuvraj
"""
from PIL.ImageOps import grayscale
from pyautogui import locateOnScreen, locateAllOnScreen, click, drag, pixel
from time import sleep
from datetime import datetime
#import win32api, win32con
#import keyboard

# we will import all necessary functions form library and my own """/#

#*** the section below finds all the locations of the all Variable for troops deployment    


def shielding():
    shield_icon=locateOnScreen('images\shield1.png', grayscale=True, region=(1750,350,300,300), confidence=0.95)
    if shield_icon != None:
        print("We have shield at{}".format(datetime.now().strftime("%c")))
        click(shield_icon.left,shield_icon.top)
        sleep(0.5)
        return False
    else:
        print("We deployed the new shield at {}".format(datetime.now().strftime("%c")))
        click( 1487,969)
        sleep(1)
        click(1140,256)
        sleep(1)
        click(1340,358)
        sleep(1)
        return True

def shield_time():
    if datetime.now().hour == 4 or datetime.now().hour == 8 or datetime.now().hour == 12 or datetime.now().hour == 16 or datetime.now().hour == 20:
        shielding()
    else:
        print("We are looking for mails")
        sleep(2)
    #print(datetime.now().hour)

if __name__ == "__main__":
    shield_time()
#tasks to do  
# 1.Test shielding fuction  re-define as per auto functions need 
# 2.Define auto shield fuction that trigger the shielding function
# 3.Define function for send rss 
# 5.Define function for gather gems 
# 6.Define function for spam help
# 7.Define function for commands