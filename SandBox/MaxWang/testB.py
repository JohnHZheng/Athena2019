#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sound import Sound
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
import math
import sys 
import time
LeftAction      = MediumMotor(OUTPUT_A)
RightAction     = MediumMotor(OUTPUT_D)
TankPair        = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
LeftSensor      = ColorSensor(INPUT_1)
RightSensor     = ColorSensor(INPUT_4)
LeftWheel       = LargeMotor(OUTPUT_B)
RightWheel      = LargeMotor(OUTPUT_C)
sound           = Sound()

def Step7():
    TankPair.on_for_seconds(SpeedDPS(200),SpeedDPS(200), 2,True,True)
    TankPair.on_for_seconds(SpeedDPS(300),SpeedDPS(300), 4.1,True,True)
    TankPair.on_for_seconds(SpeedDPS(-200),SpeedDPS(-200), 0.2,True,True)
    RightAction.on_for_degrees(-100,2100,True,True)
    #TankPair.on_for_seconds(SpeedDPS(-300),SpeedDPS(300), 2,False,True)
    
Step7()