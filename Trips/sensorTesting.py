#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

robot = AthenaRobot()
# left
robot.testColorSensor(INPUT_1, 1, 5)
# right
robot.testColorSensor(INPUT_4, 4, 5)

# left
#robot.testColorSensor(INPUT_1, 1, 5, speed=10)
# right
#robot.testColorSensor(INPUT_4, 4, 5, speed=10)
