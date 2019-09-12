#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sound import Sound
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
import time

#LeftWheel       = LargeMotor(OUTPUT_B)
#RightWheel      = LargeMotor(OUTPUT_C)
LeftAction      = MediumMotor(OUTPUT_A)
RightAction     = MediumMotor(OUTPUT_D)
TankPair        = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
LeftSensor      = ColorSensor(INPUT_1)
RightSensor     = ColorSensor(INPUT_4)
N = 0
#while N<4:
    #TankPair.on_for_seconds(SpeedDPS(-400),SpeedDPS(-400), 1)
    #TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(250),115,True,True)
    # N = N + 1

#TankPair.on_for_seconds(SpeedDPS(-500),SpeedDPS(-500), 3)
#LeftWheel.on_for_seconds(SpeedDPS(-100), 3)
#LeftAction.on_for_seconds(SpeedDPS(-500), 2, True, True)
#RightAction.on_for_seconds(SpeedDPS(-500), 2, True, True)