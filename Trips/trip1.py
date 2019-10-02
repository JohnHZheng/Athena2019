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
    robot.run(44, 20, False) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 19, scale=.15)
    robot.onUntilRightWhite(10, consecutiveHit=2,white_threshold=80)
    robot.run(9, 8)  # pushing units into place
    robot.run(-5,10)    # Revert back 5 cm
    # letting go of the attatchment
    robot.moveMediumMotor(False,-50,710)
    robot.run(-24,20) # backward for 20 centimeters
    robot.moveMediumMotor(False,50,710)# lowering down the hook

    # First Position

    robot.turnOnLeftWheel(60,10)
    robot.run(30,20)
    robot.turnOnLeftWheel(90,10)# going to the line
    # Second Postition
    #line squaring
    robot.onUntilBlackLine(black_threshold=20,consecutiveHit=2)
    robot.onUntilWhiteLine(2, white_threshold=75)
    robot.moveMediumMotor(isLeft = False,speed = 50, degrees = -385)# raising the hook
    robot.turnOnRightWheel(90)
    robot.onUntilLeftWhite(consecutiveHit=2, white_threshold=75)
    robot.run(-3,10)
    robot.turnOnLeftWheel(-15)
    robot.moveMediumMotor(False, 50, 450)
    robot.run(-10,10)
    # robot.turnOnLeftWheel(degree = -90,speed = 10)
    # robot.onUntilWhiteLine(consecutiveHit=2)# run untill reach the black corner near the tree
    #adjusting to prepare for putting on tree
    #putting blue unit in tree
    
    # robot.run(distanceCm = 10, speedCmPerSecond = -5)
    #robot.turn(-10,5)
    #robot.onUntilGameLine(consecutiveHit=2, speed=5) 
    # #hanging the bat on the tree
    # robot.moveMediumMotor(False,50,710)





    # robot.turnOnRightWheel(-100, 15)

    # robot.lineFollow(useLeftSensor = False, useLeftEdge = False, runDistanceCM = 46, scale=.12)





    """
    robot.turn(30090)
    robot.run(-7,14)

 """