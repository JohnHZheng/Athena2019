#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from helpers import getColorName

# Construct motors and robot
leftM =  Motor(Port.C)
rightM = Motor(Port.B)
robot = DriveBase (leftM,rightM, 55, 121)
# Construct Color Sensors
leftS = ColorSensor (Port.S4)
rightS = ColorSensor (Port.S1)

# Leave the starting point
robot.drive_time(300,0,400)
robot.stop(Stop.BRAKE)
# Turn right
robot.drive_time(0,90,740)
robot.stop(Stop.BRAKE)
# Drive a while to pass intermediate area
robot.drive_time(300,0,2850)
print("end of drive_time")

# Start to read Color Censor
# print( "BLACK: ", Color.BLACK)
# print( "BLUE: ", Color.BLUE)
# print( "BROWN: ", Color.BROWN)
# print( "GREEN: ", Color.GREEN)
# print( "ORANGE: ", Color.ORANGE)
# print( "PURPLE: ", Color.PURPLE)
# print( "RED: ", Color.RED)
# print( "WHITE: ", Color.WHITE)
# print( "YELLOW: ", Color.YELLOW)

lcs = leftS.color() 
print( " left: ", getColorName(lcs))
rcs = rightS.color() 
print( "right: ", getColorName(rcs))
# Stop until we see both black
while(lcs != Color.BLACK and lcs != Color.BLACK):
    robot.drive(300, 0)
    lcs = leftS.color() 
    print( " left: ", getColorName(lcs))
    rcs = rightS.color() 
    print( "right: ", getColorName(rcs))    
robot.stop(Stop.BRAKE)

""" while leftS.color() != 1:
    while rightS.color() != 1:
        Motors.drive(700,0)
Motors.stop(Stop.BRAKE)
while leftS.color() != 6:
    while rightS.color() != 6:
        Motors.drive(50,-20)
if leftS.color() == 6 and rightS.color() == 6:
    Motors.drive(150,0)
elif rightS.color() == 1:
    Motors.drive(10,75)
elif leftS.color() == 1:
    Motors.drive(10,-75)
if rightS.color() != 1 and leftS.color() != 1:
    Motors.stop(Stop.BRAKE) """
