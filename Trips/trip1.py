#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

def runTrip1(): 
    robot = AthenaRobot()
    # begin of trip constants
    white_value_left = 88
    white_value_right = 82
    black_value = 15
    mediumMotorUpDegrees = 1000
    mediumMotorDownDegrees = 1020
    mediumMotorUpSpeed = -30 
    mediumMotorDownSpeed = 50
    
    #end trip constants

    robot.run(distanceCm = 20, speedCmPerSecond = 15) 
    robot.turnRightOnLeftWheel(degree = 50)
    robot.run(20, 15) 
    robot.turnLeftOnRightWheel(50,15)  
    robot.run(20, 15) 
    robot.turnRightOnLeftWheel(-30,15) 
    for x in range(3):
        robot.turnLeftOnRightWheel(20)
        robot.turnRightOnLeftWheel(20)
    