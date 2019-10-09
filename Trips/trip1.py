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
    robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    robot.run(distanceCm = 10, speedCmPerSecond = 20, brake = False) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 26, scale=.18)
    robot.onUntilRightWhite(speed = 10, consecutiveHit=2, white_threshold = 75)
    robot.run(distanceCm = 10, speedCmPerSecond =10)  # pushing units into place
    robot.run(distanceCm = -6, speedCmPerSecond = 10)    # Revert back 5 cm
    # letting go of the attatchment
    robot.moveMediumMotor(isLeft = False, speed = -50, degrees = 710)
    robot.run(distanceCm = -26, speedCmPerSecond = 20) # backward for 28 centimeters
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 710)# lowering down the hook

    # First Position

    robot.turnOnLeftWheel(degree = 60, speed = 10)
    robot.run(distanceCm = 27, speedCmPerSecond = 20)
    robot.turnOnLeftWheel(degree = 90, speed = 10)# going to the line

    # Second Postition

    # line squaring
    robot.onUntilBlackLine(black_threshold=20,consecutiveHit=2)
    robot.onUntilWhiteLine(2, white_threshold=75)
    robot.moveMediumMotor(isLeft = False,speed = 50, degrees = -450)# raising the hook
    robot.turnOnRightWheel(degree = 95) 
    robot.run(3,10)
    robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=80)
    robot.run(distanceCm = -6, speedCmPerSecond = 10)
    robot.turnOnLeftWheel(degree = -14)
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 500)
    robot.moveMediumMotor(isLeft = False, speed = 25, degrees = -100)
    robot.run(distanceCm = -32, speedCmPerSecond = 10) 
    
    # Third Position
    

    robot.turnOnLeftWheel(degree = -35, speed = 10)#turn to face line
    robot.run(distanceCm = 42, speedCmPerSecond = 15) 
    robot.turnUntilLeftBlack(turnLeft = True, speed = 10, black_threshold = 15)
    robot.lineFollow(useLeftEdge = False, runDistanceCM = 18, scale=.12)
    robot.turnOnRightWheel(degree = 10, speed = 10)#moves crane into place
    robot.run(distanceCm = 7, speedCmPerSecond = 10)
    robot.run(distanceCm=-12,speedCmPerSecond=15)
    robot.moveMediumMotor(isLeft=False, speed=100, degrees=-500)
    robot.turnOnLeftWheel(degree=80)
    robot.run(distanceCm=-1,speedCmPerSecond=10)
    robot.moveMediumMotor(isLeft=False, speed=100, degrees=550)
    robot.run(distanceCm=3,speedCmPerSecond=10)
    robot.turnOnLeftWheel(degree=-30,speed=20)

    #Fourth Position
    