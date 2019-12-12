#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

TankPair        = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)

def runTrip1(): 
    robot = AthenaRobot()
    # begin of trip constants
    white_value_left = 80
    white_value_right = 82
    black_value = 15
    mediumMotorUpDegrees = 800
    mediumMotorDownDegrees = 900
    mediumMotorUpSpeed = 30 
    mediumMotorDownSpeed = -50

    
    # end trip constants

    # aligning the robot against crane
    robot.run(distanceCm = 25, speedCmPerSecond = 20) 
    robot.turnRightOnLeftWheel(degree = 50)
    robot.run(13, 20) 
    robot.turn(-60,10) 
    robot.run(15, 20) 
    for x in range(3):
        TankPair.on_for_seconds(SpeedDPS(-200),SpeedDPS(0),.5,True,True)
        TankPair.on_for_seconds(SpeedDPS(0),SpeedDPS(-200),.5,True,True)
    # robot.turnRightOnLeftWheel(5, 2)
    robot.run(5,20)
    robot.run(-5, 20)
    TankPair.on_for_seconds(SpeedDPS(-400),SpeedDPS(-600),.6,True,True)
    TankPair.on_for_seconds(SpeedDPS(-200),SpeedDPS(-200),.4,True,True)
    
    # putting blue block and bat in place
    robot.moveMediumMotor(isLeft = False, speed = 100, degrees = 5000, block = False) 

    # lifting the crane
    for x in range(3):
        x = 400 
        robot.moveMediumMotor(isLeft = True, speed = 75, degrees = x)
        robot.moveMediumMotor(isLeft = True, speed = 75, degrees = -x)
        robot.moveMediumMotor(isLeft = True, speed = 75, degrees = x)
        robot.moveMediumMotor(isLeft = True, speed = 75, degrees = -x)
        x = x + 50
    robot.moveMediumMotor(isLeft = False, speed = 25, degrees = 2500, block = False) 
    robot.moveMediumMotor(isLeft = True, speed = 50, degrees = 450)
    robot.moveMediumMotor(isLeft = True, speed = 75, degrees = -600)
    sleep(3.5)
    
    # retracting arm
    robot.moveMediumMotor(isLeft = False, speed = 100, degrees = -7500, block = False) 
    # moving back
    robot.run(-10, 30) 
    robot.moveMediumMotor(isLeft = True, speed = 40, degrees = mediumMotorUpDegrees)
    robot.run(-15,30)
    robot.turnRightOnRightWheel(degree=90, speed=30)
    robot.run(-55,50,brake=False)