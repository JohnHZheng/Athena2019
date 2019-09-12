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

LeftWheel       = LargeMotor(OUTPUT_B)
RightWheel      = LargeMotor(OUTPUT_C)
LeftAction      = MediumMotor(OUTPUT_D)
RightAction     = MediumMotor(OUTPUT_A)
TankPair        = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
LeftSensor      = ColorSensor(INPUT_1)
RightSensor     = ColorSensor(INPUT_4)

LoopCount           = 0
BlackTH             = 15
WhiteTH             = 80
TargetReflection    = 60
Kp                  = 2
#Right Sensor follow Right black line
while LoopCount < 1000:
    LoopCount           = LoopCount + 1
    ErrorReflection     = TargetReflection - RightSensor.reflected_light_intensity
    DeltaSpeed          = Kp * ErrorReflection
    TankPair.on(SpeedDPS(-100 - DeltaSpeed), SpeedDPS(-100 + DeltaSpeed))
    sleep(0.005)
