#!/usr/bin/env python3
from ev3dev2.button import Button 
from time import sleep
from ev3dev2.led import Leds

btn = Button() 
loop = True
leds = Leds() 
while loop:
    if btn.left == True:
        leds.set_color('LEFT','RED')
    elif btn.right == True:
        leds.set_color('RIGHT','RED')
    elif btn.up == True:
        leds.set_color('RIGHT','YELLOW')
    elif btn.down == True:
        leds.set_color('LEFT','AMBER')
    elif btn.enter == True:
        loop = False 