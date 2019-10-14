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
    # robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    # robot.run(distanceCm = 10, speedCmPerSecond = 20, brake = False) # move robot to the starting point of the line
    # # following the left edge of the line
    # robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 26, scale=.18)
    # robot.onUntilRightWhite(speed = 10, consecutiveHit=2, white_threshold = 70)
    # robot.run(distanceCm = 10, speedCmPerSecond =10)  # pushing units into place
    # robot.run(distanceCm = -5, speedCmPerSecond = 10)    # Revert back 5 cm
    # # letting go of the attatchment
    # robot.moveMediumMotor(isLeft = False, speed = -50, degrees = 710)
    # robot.run(distanceCm = -28, speedCmPerSecond = 20) # backward for 28 centimeters
    # robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 710)# lowering down the hook

    # # First Position

    # robot.turnOnLeftWheel(degree = 60, speed = 10)
    # robot.run(distanceCm = 27, speedCmPerSecond = 20)
    # robot.turnOnLeftWheel(degree = 100, speed = 10)# going to the line

    # # Second Postition

    # # line squaring
    # robot.onUntilBlackLine(black_threshold=20,consecutiveHit=2)
    # robot.onUntilWhiteLine(2, white_threshold=75)
    # robot.moveMediumMotor(isLeft = False,speed = 50, degrees = -550)# raising the hook
    # robot.turnOnRightWheel(degree = 90) 
    # robot.onUntilLeftBlack(consecutiveHit=2)
    # robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=60)
    # robot.run(distanceCm = -3, speedCmPerSecond = 10)
    # robot.turnOnLeftWheel(degree = -18)
    # robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 550)
    # robot.moveMediumMotor(isLeft = False, speed = 25, degrees = -150)
    # robot.run(distanceCm = -32, speedCmPerSecond = 10) 
    
    # # # Third Position
    
    # robot.turnOnLeftWheel(degree = -35, speed = 10)#turn to face line
    # robot.run(distanceCm = 40, speedCmPerSecond = 15) 
    # robot.turnUntilLeftBlack(turnLeft = True, speed = 10, black_threshold = 15)
    # robot.lineFollow(useLeftEdge = False, runDistanceCM = 18, scale=.12)
    # robot.turnOnRightWheel(degree = 10, speed = 10)#moves crane into place
    # robot.run(distanceCm = 7, speedCmPerSecond = 10)
    # robot.run(distanceCm=-12,speedCmPerSecond=15)
    # robot.moveMediumMotor(isLeft=False, speed=100, degrees=-500)
    # robot.turnOnLeftWheel(degree=80)
    # robot.run(distanceCm=-1,speedCmPerSecond=10)
    # robot.moveMediumMotor(isLeft=False, speed=100, degrees=550)
    # robot.run(distanceCm=3,speedCmPerSecond=10)
    # robot.turnOnLeftWheel(degree=-30,speed=20)

    # #Fourth Position

    # robot.run(distanceCm = 8, speedCmPerSecond = 8) 
    # robot.moveMediumMotor(isLeft = False, speed = 50, degrees = -600,block=True) #picking up the drone
    # sleep(1)
    # robot.turnOnLeftWheel(degree = 15)
    # robot.run(4, 5)
    # robot.run(-4,5) 
    # robot.turnOnRightWheel(30,5)
    # robot.run(-60,25)
    # robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 600) 
    
    # Fifth Position

    robot.turnUntilLeftWhite(True,10,white_threshold=70)
    robot.turn(5)
    
    robot.lineFollow(useLeftSensor=True,useLeftEdge=True, runDistanceCM=8,)
    robot.turnOnRightWheel(-35, 20)
    robot.run(5, 10)
    robot.onUntilWhiteLine(consecutiveHit=2,white_threshold=70)
    robot.onUntilBlackLine(consecutiveHit=2, black_threshold = 20) 
    robot.run(2,10) 
    robot.turnUntilRightBlack(turnLeft = False, speed = 5) 
