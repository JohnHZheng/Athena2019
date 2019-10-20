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
    white_value = 80
    black_value = 15
    robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    robot.run(distanceCm = 10, speedCmPerSecond = 20, brake = False) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 16, scale=.18)
    robot.onUntilRightWhite(speed = 10, consecutiveHit=2, white_threshold = white_value)
    robot.run(distanceCm = 10, speedCmPerSecond =10)  # pushing units into place
    robot.run(distanceCm = -5, speedCmPerSecond = 10)    # Revert back 5 cm
    # letting go of the attatchment
    robot.moveMediumMotor(isLeft = False, speed = -50, degrees = 710)
    robot.run(distanceCm = -28, speedCmPerSecond = 20) # backward for 28 centimeters
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 710)# lowering down the hook

    # First Position
    sleep(1)

    robot.turnOnLeftWheel(degree = 60, speed = 10)
    robot.run(distanceCm = 27, speedCmPerSecond = 20)
    robot.turnOnLeftWheel(degree = 100, speed = 10)# going to the line

    # Second Postition
    sleep(1)
    # line squaring
    robot.onUntilBlackLine(black_threshold=black_value,consecutiveHit=1)
    robot.onUntilWhiteLine(white_threshold=white_value, consecutiveHit=1)
    robot.moveMediumMotor(isLeft = False,speed = 50, degrees = -550) # raising the hook
    robot.turnOnRightWheel(degree = 100) 
    robot.run(distanceCm=-3, speedCmPerSecond=10)
    robot.onUntilLeftBlack(consecutiveHit=2,black_threshold=black_value)
    robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=white_value)
    robot.run(distanceCm = -2, speedCmPerSecond = 10)
    robot.turnOnLeftWheel(degree = -18)
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 550)
    robot.moveMediumMotor(isLeft = False, speed = 25, degrees = -50)
    robot.run(distanceCm = -32, speedCmPerSecond = 10) 
    
    # Third Position
    sleep(1)
    robot.turnOnLeftWheel(degree = -35, speed = 10)#turn to face line
    robot.run(distanceCm = 40, speedCmPerSecond = 15) 
    robot.turnUntilLeftBlack(turnLeft = True, speed = 10, black_threshold = black_value)
    robot.lineFollow(useLeftEdge = False, runDistanceCM = 17, scale=.12)
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
    sleep(1)
    robot.run(distanceCm = 8, speedCmPerSecond = 8) 
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = -600,block=True) #picking up the drone
    sleep(0.5)
    robot.turnOnLeftWheel(degree = 15)
    robot.run(distanceCm = 4,speedCmPerSecond = 5)
    robot.run(distanceCm = -2,speedCmPerSecond = 5) 
    robot.turnOnRightWheel(degree = 30,speed = 5)
    robot.run(distanceCm = -13,speedCmPerSecond = 15)
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 600,block=True)
    sleep(0.5)
    robot.run(-44,20) 

    # Fifth Position
    sleep(1)
    robot.onUntilLeftWhite(speed=-5, white_threshold=white_value)
    robot.run(5,10)
    robot.turnUntilLeftWhite(turnLeft=True,speed=10,white_threshold=white_value)
    robot.lineFollow(whiteThreshold=75,useLeftSensor=True, useLeftEdge=True, runDistanceCM=15)
    robot.onUntilBlackLine(consecutiveHit=2,black_threshold=black_value)
    robot.onUntilWhiteLine(consecutiveHit=2,white_threshold=white_value)
    robot.moveMediumMotor(isLeft = False, speed = 100, degrees = -400)
    sleep(0.5)
    robot.revertSafely()
    robot.turnOnLeftWheel(120,20)
    robot.revertSafely()