#!/usr/bin/env python3
from ev3dev2.button import Button 
from time import sleep
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
import os
import sys
os.system('setfont Lat15-TerminusBold14')

btn = Button() 
loop = True
leds = Leds() 
sound = Sound() 
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
    else:
        print('Do something!')
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1300, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1700, 1)
sleep(0.5)
sound.play_tone(1700, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1300, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1500, 1)
sleep(0.5)
sound.play_tone(1400, 1)
sleep(0.5)
sound.play_tone(1300, 1)
