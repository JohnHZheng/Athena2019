#!/usr/bin/env python3
from ev3dev2.button import Button
from time import sleep
from trip1 import runTrip1
from trip2 import PanelDemo
btn = Button()
contin = True
while contin:
   
    if btn.left == True:
        PanelDemo()
    elif btn.up == True:
        runTrip1()
    elif btn.enter == True:
        contin = False