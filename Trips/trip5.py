#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

def runTrip5(): 
    robot = AthenaRobot()
    # begin of trip constants
    white_value_left = 84
    white_value_right = 82
    black_value = 15
    mediumMotorUpDegrees = 1000
    mediumMotorDownDegrees = 1020
    mediumMotorUpSpeed = -30 
    mediumMotorDownSpeed = 50
    # end of trip constants
    
    robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    robot.run(distanceCm = 10, speedCmPerSecond = 20, brake = False) # move robot to the starting point of the line
    
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 17, scale=.18)
    robot.onUntilRightLighterBy(difference = 20 , white_threshold= white_value_right)
    robot.run(distanceCm = 10, speedCmPerSecond =10)     # pushing units into place
    robot.run(distanceCm = -5, speedCmPerSecond = 20)   # Revert back 5 cm
    
    # letting go of the attachment
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorUpSpeed, degrees = mediumMotorUpDegrees)
    robot.run(distanceCm = -27, speedCmPerSecond = 20) # backward for 28 centimeters
    
    # First Position
    robot.turnRightOnLeftWheel(degree = 18, speed = 10)  # turn right
    robot.run(distanceCm = 5, speedCmPerSecond = 10)
    robot.turnUntilLeftWhite(turnLeft=True,speed = 10,white_threshold = white_value_left)
    robot.lineFollow(whiteThreshold = white_value_right, useLeftSensor = True, useLeftEdge = True, runDistanceCM = 12, scale=.15)
    robot.onUntilBlackLine(consecutiveHit = 2,black_threshold = black_value)
   