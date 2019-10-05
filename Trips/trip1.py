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
    robot.run(75, 30)
    robot.run(-75, 30)
def Trip1Tryout(): 
    robot = AthenaRobot()
    robot.run(44, 15, False) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 19, scale=.15)
    robot.onUntilRightWhite(10, consecutiveHit=2,white_threshold=80)
    robot.run(9, 8)  # pushing units into place
    robot.run(-5,10)    # Revert back 5 cm
    # letting go of the attatchment
    robot.moveMediumMotor(False,-50,710)
    robot.run(-28,20) # backward for 20 centimeters
    robot.moveMediumMotor(False,50,710)# lowering down the hook

    # First Position

    robot.turnOnLeftWheel(60,10)
    robot.run(27,20)
    robot.turnOnLeftWheel(90,10)# going to the line

    # Second Postition

    #line squaring
    robot.onUntilBlackLine(black_threshold=20,consecutiveHit=2)
    robot.onUntilWhiteLine(2, white_threshold=75)
    robot.moveMediumMotor(isLeft = False,speed = 50, degrees = -450)# raising the hook
    robot.turnOnRightWheel(90)
    robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=75)
    robot.run(-3,10)
    robot.turnOnLeftWheel(-15)
    robot.moveMediumMotor(False, 50, 450)
    robot.moveMediumMotor(False,25,-100)
    robot.run(-10,10)
    

    #Third Position

    #robot.turnOnRightWheel(90,20) 
    