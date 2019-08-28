#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def lineFollow():
    # need wheel motor on Port B and C, and two color sensors on Port 1 and 4
    left =  Motor(Port.C)
    right = Motor(Port.B)
    Motors = DriveBase (left,right, 55, 121)
    leftS = ColorSensor (Port.S4)
    rightS = ColorSensor (Port.S1)    
    while True:
        if leftS.color() == 6 and rightS.color() == 6:
            Motors.drive(150,0)
        elif rightS.color() == 1:
            Motors.drive(10,75)
        elif leftS.color() == 1:
            Motors.drive(10,-75)

def advLineFollow(speed1, speed2, degree):
    # need wheel motor on Port B and C, and two color sensors on Port 1 and 4
    left =  Motor(Port.C)
    right = Motor(Port.B)
    Motors = DriveBase (left,right, 55, 121)
    leftS = ColorSensor (Port.S4)
    rightS = ColorSensor (Port.S1)    
    while True:
        if leftS.color() == 6 and rightS.color() == 6:
            Motors.drive(200,0)
        elif rightS.color() == 1:
            Motors.drive(10,75)
        elif leftS.color() == 1:
            Motors.drive(10,-75)

def getColorName(colorInt):
    switcher = {
        1: "Black",
        2: "Blue",
        3: "Green",
        4: "Yellow",
        5: "Red",
        6: "White",
        7: "Brown",
        8: "Orange",
        9: "Purple",
    }
    return '{0}:{1}'.format( switcher.get(colorInt, "Invalid color"), colorInt)