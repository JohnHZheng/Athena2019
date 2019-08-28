#!/usr/bin/env micropython
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
from trip1 import runTrip1
from trip2 import runTrip2
from trip3 import runTrip3
from trip4 import runTrip4
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')
sound = Sound()

print('Up for Trip 2')
print('Left for Trip 1')
print('Right for Trip 3')
print('Down for Trip 4')
sound.beep()
btn = Button()
contin = True
while contin:
   
    if btn.left == True:
        runTrip1()
    elif btn.up == True:
        runTrip2()
    elif btn.right == True:
        runTrip3()
    elif btn.down == True:
        runTrip4()                
    elif btn.enter == True:
        contin = False