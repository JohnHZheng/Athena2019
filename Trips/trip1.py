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
    white_value_left = 90
    white_value_right = 80
    black_value = 12
    mediumMotorUpDegrees = 800
    mediumMotorDownDegrees = 510 
    mediumMotorUpSpeed = -30 
    mediumMotorDownSpeed = 50
    # end of trip constants
    
    robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) # move robot to the starting point of the line
    robot.run(distanceCm = 10, speedCmPerSecond = 20, brake = False) # move robot to the starting point of the line
    
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 16, scale=.18)
    robot.onUntilRightWhite(speed = 10, consecutiveHit = 2, white_threshold = white_value_right)
    robot.run(distanceCm = 9, speedCmPerSecond =10)     # pushing units into place
    robot.run(distanceCm = -5, speedCmPerSecond = 20)   # Revert back 5 cm
    
    # letting go of the attachment
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorUpSpeed, degrees = mediumMotorUpDegrees)
    robot.run(distanceCm = -27, speedCmPerSecond = 20) # backward for 28 centimeters
    
    # First Position
    robot.turnOnLeftWheel(degree = 60, speed = 10)  # turn right
    robot.run(distanceCm = 24, speedCmPerSecond = 20)
    robot.turnOnRightWheel(degree = 70, speed = 10)  #turn to face line

    # Third Position
    robot.turnUntilLeftBlack(speed = 8, black_threshold = black_value, turnLeft = True)
    robot.run(distanceCm = 0.5, speedCmPerSecond = 10) 
    robot.lineFollow(useLeftEdge = False, runDistanceCM = 16, scale = .12)
    robot.turnOnRightWheel(degree = 10, speed = 10)     # moves crane into place
    robot.run(distanceCm = 7, speedCmPerSecond = 15)
    robot.onUntilRightBlack(speed = -15, consecutiveHit = 2, black_threshold = black_value)  # backward until black on right for IOC
    robot.run(distanceCm = -3,speedCmPerSecond = 20)
    robot.turnOnLeftWheel(degree = 78)                  # this will put the hoop of bat to the branch
    robot.run(distanceCm = -1,speedCmPerSecond = 10)    # backward a little bit
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorDownSpeed, degrees = mediumMotorDownDegrees)   # lower down 
    robot.run(distanceCm = 3,speedCmPerSecond = 10)     # push forward a little bit
    robot.turnOnLeftWheel(degree = -30,speed = 10)      # turn to the drone

    # Fourth Position
    sleep(0.1)  # pause to settle down
    robot.onUntilWhiteLine(consecutiveHit = 1, speed = -10, white_threshold = white_value_right)
    robot.turn(degree = -6) # turn left a bit
    robot.run(distanceCm = 12, speedCmPerSecond = 12) 
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorUpSpeed, degrees = mediumMotorUpDegrees, block=True) #picking up the drone
    sleep(0.1)
    robot.turnOnLeftWheel(degree = 15, speed = 6)
    robot.run(distanceCm = 4, speedCmPerSecond = 8)
    robot.run(distanceCm = -3, speedCmPerSecond = 8) 
    robot.turnOnRightWheel(degree = 30,speed = 5)
    robot.run(distanceCm = -13,speedCmPerSecond = 15)
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorDownSpeed, degrees = mediumMotorDownDegrees, block = True)
    sleep(0.1)
    # TODO: THe following three lines are not tested yet
    robot.onUntilWhiteLine(consecutiveHit=2, speed = -10, white_threshold = white_value_right)   # line square on white to get angle
    robot.turn(degree = 10) # turn left a bit
    robot.run(distanceCm = -40, speedCmPerSecond = 20) 

    # Fifth Position
    robot.onUntilLeftWhite(speed = -10, white_threshold = white_value_left)
    robot.run(distanceCm = 5, speedCmPerSecond = 10)
    robot.turnUntilLeftWhite(turnLeft=True,speed = 10,white_threshold = white_value_left)
    robot.lineFollow(whiteThreshold = white_value_right, useLeftSensor = True, useLeftEdge = True, runDistanceCM = 12)
    robot.onUntilBlackLine(consecutiveHit = 2,black_threshold = black_value)
    robot.onUntilWhiteLine(consecutiveHit = 2,white_threshold = white_value_right)
    robot.moveMediumMotor(isLeft = False, speed = 100, degrees = -400)
    sleep(0.5)

    # # go back to base
    # robot.revertSafely()
    # robot.turnOnLeftWheel(degree = 120, speed = 20)
    # robot.revertSafely()

    # # trial of parking on bridge
    # robot.turn(degree = 115)
    # robot.run(distanceCm = 18, speedCmPerSecond = 20)
    # robot.onUntilWhiteLine(consecutiveHit = 1, speed = 5, white_threshold = white_value_right)
    # robot.onUntilBlackLine(consecutiveHit = 1, speed = 5, black_threshold = black_value)
    # robot.turn(degree = -47)
    # robot.run(distanceCm = 35, speedCmPerSecond = 20)
    # robot.turn(degree = -25)
    # robot.onUntilGameLine(consecutiveHit = 1, speed = 5, white_threshold = white_value_right, black_threshold = black_value)
    # robot.onUntilWhiteLine(consecutiveHit = 1, white_threshold = white_value_right)
    # robot.run(distanceCm = 13,speedCmPerSecond = 15)
    # robot.turnOnLeftWheel(degree = -93)
    # robot.run(distanceCm = -15, speedCmPerSecond = 20)
    # robot.run(distanceCm = 50, speedCmPerSecond = 60)