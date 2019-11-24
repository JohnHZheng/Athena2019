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
TankPair.on_for_degrees(SpeedDPS(-105),SpeedDPS(-100), 685,False,True)
TankPair.on_for_degrees(SpeedDPS(100),SpeedDPS(100), 250,True,True)
TankPair.on_for_degrees(SpeedDPS(300),SpeedDPS(300), 100,True,True)
TankPair.on_for_degrees(SpeedDPS(-300),SpeedDPS(300), 150,True,True)
TankPair.on_for_degrees(SpeedDPS(300),SpeedDPS(300), 550,True,True)
TankPair.on_for_degrees(SpeedDPS(300),SpeedDPS(-300), 180,True,True)
