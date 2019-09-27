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
    
    #robot.run(43,20) # move robot to the starting point of the line
    # following the left edge of the line
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 17, scale=.15)
    # robot.run(20,8) # pushing units into place
    # robot.run(5,-10)
    # # letting go of the attatchment
    # robot.moveMediumMotor(False,-50,710)
    # robot.run(30,-20) #backward for 24 centimeters
    
    # #hanging the bat on the tree
    # robot.moveMediumMotor(False,50,710)





    # robot.turnOnRightWheel(-100, 15)

    # robot.lineFollow(useLeftSensor = False, useLeftEdge = False, runDistanceCM = 46, scale=.12)





    """
    robot.turn(30090)
    robot.run(-7,14)

 """