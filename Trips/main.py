#!/usr/bin/env micropython
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
from trip1 import runTrip1, Trip1Tryout
from trip2 import runTrip2
from trip3 import runTrip3
from trip4 import runTrip4
from trip5 import runTrip5
from time import sleep
import os
os.system('setfont Uni3-TerminusBold16')
sound = Sound()

btn = Button()
contin = True
print('*** ATHENA ROCKS! ***')
print('1 - Left for Trip 1')
print('2 - Up for Trip 2')
print('3 - Right for Trip 3')
print('4 - Down for Trip 4')
print('5 - Center to Exit')
sound.beep()
while contin:

    if btn.left == True:
        runTrip1()
        sound.beep()
    elif btn.up == True:
        runTrip2()
        sound.beep()
    elif btn.right == True:
        runTrip3()
        sound.beep()
    elif btn.down == True:
        runTrip4()
        sound.beep()
    elif btn.enter == True:
        runTrip5()
        sound.beep()