#!/usr/bin/env python3
from ev3dev2.button import Button 
from time import sleep
from ev3dev2.led import Leds

btn = Button() 
loop = True
color = ['RED']
while loop = True:
    if btn.enter == True:
        leds.set_color(color)
    elif btn.right == True:
        loop = False


