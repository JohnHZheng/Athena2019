#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
def runTrip4():
    # Circle
    leftWheel = Motor(Port.B)
    rightWheel = Motor(Port.C)
    robot = DriveBase(leftWheel,rightWheel,100,156)
    robot.drive_time(100,100,5000)