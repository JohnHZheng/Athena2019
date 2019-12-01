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
    white_value_left = 80
    white_value_right = 82
    black_value = 15
    mediumMotorUpDegrees = 800
    mediumMotorDownDegrees = 800
    mediumMotorUpSpeed = 30 
    mediumMotorDownSpeed = -50
    
    # end trip constants

    # aligning the robot against crane
    robot.run(distanceCm = 10, speedCmPerSecond = 10) 
    robot.turnRightOnLeftWheel(degree = 50)
    robot.run(17.5, 15) 
    robot.turnLeftOnRightWheel(70,10) 
    # robot.run(22, 15) 
    # for x in range(5):
    #     robot.turnRightOnLeftWheel(20, speed = 10)
    #     robot.turnLeftOnRightWheel(20, speed = 10)
    # robot.turnRightOnLeftWheel(5, 2)
    # robot.run(-10, 20)
    # robot.run(15,30)
    # # putting blue block and bat in place
    # robot.moveMediumMotor(isLeft = False, speed = 100, degrees = 4000, block = False) 

    # # lifting the crane
    # for x in range(3): 
    #     robot.moveMediumMotor(isLeft = True, speed = 75, degrees = 450)
    #     robot.moveMediumMotor(isLeft = True, speed = 75, degrees = -450)
    # robot.moveMediumMotor(isLeft = False, speed = 25, degrees = 3500, block = False) 
    # robot.moveMediumMotor(isLeft = True, speed = 50, degrees = mediumMotorUpDegrees) 

    # # moving back
    # robot.run(-10, 15) 
    # robot.moveMediumMotor(isLeft = True, speed = 40, degrees = mediumMotorDownDegrees)
