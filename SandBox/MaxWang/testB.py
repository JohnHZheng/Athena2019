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
LeftAction      = MediumMotor(OUTPUT_A)
RightAction     = MediumMotor(OUTPUT_D)
TankPair    	= MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
#TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),715,True,True)
#TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),715,True,True)
"""
n = 0
while n<4:
	TankPair    	= MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
	TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-250),250 )
	n=n+1
n = 0
while n<4:
	TankPair    	= MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
	TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(250),260 )
	n=n+1
"""

LeftAction.on_for_seconds(100, 0.6)
sleep(2)
LeftAction.on_for_seconds(100, 0.6)
sleep(2)
LeftAction.on_for_seconds(-100, 1.2)