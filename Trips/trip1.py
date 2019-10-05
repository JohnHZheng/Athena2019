#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

# wheel constances in Center Meter
wheelRadiusCm = 2.75 
wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
leftMotor = LargeMotor(OUTPUT_C)
rightMotor = LargeMotor(OUTPUT_B) 
leftSensor = ColorSensor(INPUT_4)
rightSensor = ColorSensor(INPUT_1)
forkliftMtr= MediumMotor(OUTPUT_D)

def runTrip1(): 
    robot = AthenaRobot()
    robot.run(distanceCm = 44, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 19, scale=.15)
    robot.onUntilRightWhite(speed = 10, consecutiveHit=2,white_threshold=80)
    robot.run(distanceCm = 9, speedCmPerSecond = 8)  # pushing units into place
    robot.run(distanceCm = -5, speedCmPerSecond = 10)    # Revert back 5 cm
    # letting go of the attatchment
    robot.moveMediumMotor(isLeft = False, speed = -50, degrees = 710)
    robot.run(distanceCm = -28, speedCmPerSecond = 20) # backward for 28 centimeters
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 710)# lowering down the hook

    # First Position

    robot.turnOnLeftWheel(degree = 60, speed = 10)
    robot.run(distanceCm = 27, speedCmPerSecond = 20)
    robot.turnOnLeftWheel(degree = 90, speed = 10)# going to the line

    # Second Postition

    #line squaring
    robot.onUntilBlackLine(black_threshold=20,consecutiveHit=2)
    robot.onUntilWhiteLine(2, white_threshold=75)
    robot.moveMediumMotor(isLeft = False,speed = 50, degrees = -450)# raising the hook
    robot.turnOnRightWheel(degree = 90)
    robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=75)
    robot.run(distanceCm = -3, speedCmPerSecond = 10)
    robot.turnOnLeftWheel(degree = -15)
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 450)
    robot.moveMediumMotor(isLeft = False, speed = 25, degrees = -100)
    robot.run(distanceCm = -10, speedCmPerSecond = 10)
    

    #Third Position

    #robot.turnOnRightWheel(90,20) 
    