#!/usr/bin/env python3
from ev3dev2.button import Button
from time import sleep
from trip1 import runTrip1
from trip2 import runTrip2
from trip3 import runTrip3
from trip4 import runTrip4

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