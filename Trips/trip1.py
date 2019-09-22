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
    wheelRadiusCm = 4
    wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
    leftMotor = LargeMotor(OUTPUT_C)
    rightMotor = LargeMotor(OUTPUT_B)
    leftSensor = ColorSensor(INPUT_4)
    rightSensor = ColorSensor(INPUT_1)
    forkliftMtr= MediumMotor(OUTPUT_D)
    robot = AthenaRobot()
    robot.testRobot()
    #robot.lineFollow(useRightSensor=False,runDistanceCM=50, leftEdge= False, scale=.1)
    #robot.run(55,-23)
    # robot.lineFollow(useRightSensor=False,runDistanceCM=20, reverse= True)
    # robot.turnOnLeftWheel(1200,-20,block=False)
    # robot.turnOnRightWheel(1200,-20.5)


    """
    robot.turn(30090)
    robot.run(-7,14)

 """
    