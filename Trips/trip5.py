#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
import math
import sys 
from athenaRobot import AthenaRobot

def runTrip5():
    #sound = Sound()
    #sound.speak('This is trip five. More to come...', espeak_opts='-a 200 -s 130 -ven+m7', volume=100)
    robot = AthenaRobot()
    robot.turnOnLeftWheel(-90)