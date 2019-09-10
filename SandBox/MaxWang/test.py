#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor

lmB = LargeMotor(OUTPUT_B)
lmC = LargeMotor(OUTPUT_C)


A = 0
while A<4:
    lmB.on_for_seconds(MoveTank(-50), 2.25, True, False)
    lmC.on_for_seconds(MoveTank(-50), 2.25)
     lmB.on_for_seconds(MoveTank(-100), 2.25, True, False)
    lmC.on_for_seconds(MoveTank(-50), 2.25) 
    A = A+1
    
    


