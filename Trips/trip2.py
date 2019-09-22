#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

def runTrip2():
        wheelRadiusCm = 4
        wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
        leftMotor = LargeMotor(OUTPUT_C)
        rightMotor = LargeMotor(OUTPUT_B) 
        leftSensor = ColorSensor(INPUT_4)
        rightSensor = ColorSensor(INPUT_1)
        forkliftMtr= MediumMotor(OUTPUT_D)
        robot = AthenaRobot()
        forkliftMtr.on(30)
        sleep(1)
        forkliftMtr.off()
        forkliftMtr.on(-30)
        sleep(1)
        forkliftMtr.off()