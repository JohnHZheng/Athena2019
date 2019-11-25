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
ound           = Sound()
def Step1():
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-150), 100,True,True)
def Step2():
    TankPair.on_for_degrees(SpeedDPS(-300),SpeedDPS(-300), 385,True,True)
    """
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    while LeftSensor.color != 6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    """
    TankPair.on_for_degrees(SpeedDPS(-150),SpeedDPS(0), 110,True,True)
    TankPair.on_for_degrees(SpeedDPS(-300),SpeedDPS(-300), 950,True,True)
def Step3():
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200), 45,True,True)
    RightAction.on_for_degrees(-60,600,True,True)
def Step4():
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    while RightSensor.color != 1:
        TankPair.on(SpeedDPS(0),SpeedDPS(-200))
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-200), 175,True,True)
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(-200), 225,True,True)


Step1()
Step2()
Step3()
Step4()
