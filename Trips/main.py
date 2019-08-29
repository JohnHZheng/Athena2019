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
os.system('setfont Uni3-TerminusBold16')
sound = Sound()

print('*** ATHENA ROCKS! ***')
print('1 - Left for Trip 1')
print('2 - Up for Trip 2')
print('3 - Right for Trip 3')
print('4 - Down for Trip 4')
print('5 - Center to Exit')
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