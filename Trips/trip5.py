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
    white_value_left = 90
    white_value_right = 80
    black_value = 12
    mediumMotorWithBlueUnitUpDegrees = 900 
    mediumMotorUpDegrees = 600
    mediumMotorDownDegrees = 510 
    mediumMotorUpSpeed = -30 
    mediumMotorDownSpeed = 50

    # end of trip constants
    
    robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    robot.run(distanceCm = 10, speedCmPerSecond = 20, brake = False) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 16, scale=.18)
    robot.onUntilRightWhite(speed = 10, consecutiveHit=2, white_threshold = white_value_right)
    robot.run(distanceCm = 10, speedCmPerSecond =10)  # pushing units into place
    robot.run(distanceCm = -5, speedCmPerSecond = 10)    # Revert back 5 cm
    # letting go of the attatchment
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorUpSpeed, degrees = mediumMotorWithBlueUnitUpDegrees)
    robot.run(distanceCm = -28, speedCmPerSecond = 20) # backward for 28 centimeters
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorDownSpeed, degrees = mediumMotorDownDegrees)# lowering down the hook

    # First Position
    sleep(1)

    robot.turnOnLeftWheel(degree = 60, speed = 10)
    robot.run(distanceCm = 27, speedCmPerSecond = 20)
    robot.turnOnLeftWheel(degree = 100, speed = 10)# going to the line

    # Second Postition
    sleep(1)
    # line squaring
    robot.onUntilBlackLine(black_threshold=black_value,consecutiveHit=1)
    robot.onUntilWhiteLine(white_threshold=white_value_right, consecutiveHit=1)
    robot.moveMediumMotor(isLeft = False,speed = mediumMotorUpSpeed, degrees = mediumMotorWithBlueUnitUpDegrees) # raising the hook
    robot.turnOnRightWheel(degree = 107) 
    robot.run(distanceCm=-4, speedCmPerSecond=10)
    robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=white_value_left)
    robot.onUntilLeftBlack(consecutiveHit=2,black_threshold=black_value) 
    robot.run(distanceCm = -4, speedCmPerSecond = 7) 
    robot.moveMediumMotor(isLeft = False, speed = 50, degrees = 550) 
    robot.turnOnRightWheel(5) 
    robot.moveMediumMotor(isLeft = False, speed = 25, degrees = -80) 
    robot.run(distanceCm=-10, speedCmPerSecond=8) 
    robot.run(distanceCm = -30, speedCmPerSecond = 20)

    robot.turnOnRightWheel(degree = 45) 
    robot.onUntilBlackLine(consecutiveHit = 2, black_threshold = black_value) 
    
    # Third Position
    sleep(1)
    robot.turnOnLeftWheel(degree = -35, speed = 10)#turn to face line
    robot.run(distanceCm = 30, speedCmPerSecond = 15) 
    robot.turnUntilLeftBlack(turnLeft = True, speed = 10, black_threshold = black_value)
    robot.lineFollow(useLeftEdge = False, runDistanceCM = 17, scale=.12)
    robot.turnOnRightWheel(degree = 10, speed = 10)#moves crane into place
    robot.run(distanceCm = 7, speedCmPerSecond = 10)
    robot.run(distanceCm=-12,speedCmPerSecond=15)
    robot.moveMediumMotor(isLeft=False, speed=mediumMotorUpSpeed, degrees=mediumMotorUpDegrees)
    robot.turnOnLeftWheel(degree=80)
    robot.run(distanceCm=-1,speedCmPerSecond=10)
    robot.moveMediumMotor(isLeft=False, speed=mediumMotorDownSpeed, degrees=mediumMotorDownDegrees)
    robot.run(distanceCm=3,speedCmPerSecond=10)
    robot.turnOnLeftWheel(degree=-30,speed=20)

    # Fourth Position
    sleep(1)
    robot.run(distanceCm = 8, speedCmPerSecond = 8) 
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorUpSpeed, degrees = mediumMotorUpDegrees,block=True) #picking up the drone
    sleep(0.5)
    robot.turnOnLeftWheel(degree = 15)
    robot.run(distanceCm = 4,speedCmPerSecond = 5)
    robot.run(distanceCm = -3,speedCmPerSecond = 5) 
    robot.turnOnRightWheel(degree = 30,speed = 5)
    robot.run(distanceCm = -13,speedCmPerSecond = 15)
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorDownSpeed, degrees = mediumMotorDownDegrees,block=True)
    sleep(0.5)
    robot.run(-44,20) 

    # Fifth Position
    sleep(1)
    robot.onUntilLeftWhite(speed=-5, white_threshold=white_value_left)
    robot.run(5,10)
    robot.turnUntilLeftWhite(turnLeft=True,speed=10,white_threshold=white_value_left)
    robot.lineFollow(whiteThreshold=75,useLeftSensor=True, useLeftEdge=True, runDistanceCM=13)
    robot.onUntilBlackLine(consecutiveHit=2,black_threshold=black_value)
    robot.onUntilWhiteLine(consecutiveHit=2,white_threshold=white_value_right)
    robot.moveMediumMotor(isLeft = False, speed = 100, degrees = -400)
    sleep(0.5)
    robot.revertSafely()
    robot.turnOnLeftWheel(120,20)
    robot.revertSafely()