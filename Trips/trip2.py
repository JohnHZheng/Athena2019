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
def runTrip2():
    TankPair.on_for_degrees(SpeedDPS(-140),SpeedDPS(-100), 900,False,True)
#    TankPair.on_for_degrees(SpeedDPS(-100),SpeedDPS(-100), 200,False,True)
    TankPair.on_for_degrees(SpeedDPS(50),SpeedDPS(50), 150,True,True)
    TankPair.on_for_degrees(SpeedDPS(400),SpeedDPS(400), 250,True,True)
    TankPair.on_for_degrees(SpeedDPS(-400),SpeedDPS(400), 200,True,True)
    TankPair.on_for_degrees(SpeedDPS(400),SpeedDPS(400), 600,True,True)
    TankPair.on_for_degrees(SpeedDPS(400),SpeedDPS(-400), 300,True,True)
    LeftAction.on_for_degrees(0,0,False,False)
    RightAction.on_for_degrees(0,0,False,False)
    
