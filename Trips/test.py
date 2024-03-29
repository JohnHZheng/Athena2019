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

# Test Medium Motors
robot.moveMediumMotor(isLeft = False, speed = -30, degrees = 1000)
sleep(1)
robot.moveMediumMotor(isLeft = False, speed = 20, degrees = 1020)

# Test Turns
robot.turnRight(90)
robot.turnLeft(90)
sleep(0.5)
robot.turnRightOnRightWheel(90)
robot.turnLeftOnRightWheel(90)
sleep(0.5)
robot.turnRightOnLeftWheel(90)
robot.turnLeftOnLeftWheel(90)


