# -*- coding: utf-8 -*-
"""
Created on Thu June 3 2:56 2021

@author: Yuvraj
"""
from pyautogui import click
from time import sleep
#we will take the coordinates from the guild chat

def send_ore():
    click(1050,550)
    sleep(1)
    click(825,766)
    sleep(1)
    click(995,932)
    sleep(2)
    click(1487,1019)
    sleep(1)
    click(1118,554)
    sleep(9)
    #read location from mail and verify the mail is from the owner of the farm
    
def send_food():
    click(1050,550)
    sleep(1)
    click(825,766)
    sleep(1)
    click(995,495)
    sleep(2)
    click(1487,1019)
    sleep(1)
    click(1118,554)
    sleep(9)

def send_stone():
    click(1050,550)
    sleep(1)
    click(825,766)
    sleep(1)
    click(995,645)
    sleep(2)
    click(1487,1019)
    sleep(1)
    click(1118,554)
    sleep(9)
def send_wood():
    click(1050,550)
    sleep(1)
    click(825,766)
    sleep(1)
    click(995,788)
    sleep(2)
    click(1487,1019)
    sleep(1)
    click(1118,554)
    sleep(9)
    #go to the map and find owner 
    #click on castle -> click on profile

if __name__=='__main__':
    sleep(5)
    for i in range(5):
        send_ore()