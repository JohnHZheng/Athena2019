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
        robot = AthenaRobot()
        # with blue unit perfect up and down of forklift
        robot.moveMediumMotor(isLeft = False, speed = -30, degrees = 900)
        sleep(1)
        robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 510)

        # without blue unit perfect up and down of forklift
        robot.moveMediumMotor(isLeft = False, speed = -30, degrees = 600)
        sleep(1)
        robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 510)
