#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound
from athenaRobot import AthenaRobot
import random

def runTrip4():
    robot = AthenaRobot()
    white_value_left = 88
    white_value_right = 82
    black_value = 12
    robot.run(distanceCm = 43, speedCmPerSecond = 20)
    robot.turnUntilLeftWhite(turnLeft=True,speed = 7,white_threshold = white_value_left)
    robot.lineFollow(whiteThreshold = white_value_right, useLeftSensor = True, useLeftEdge = True, runDistanceCM = 12)
    robot.onUntilBlackLine(consecutiveHit = 2,black_threshold = black_value)
    robot.run(3,5)
    robot.moveMediumMotor(isLeft = False, speed = 100, degrees = -800)
    sleep(0.5) 
    robot.revertSafely()
    robot.turn(120, 15)
    robot.revertSafely() 