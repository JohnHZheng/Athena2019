#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
  
def runTrip2():
    # Square
    left =  Motor(Port.C)
    right = Motor(Port.B)
    Motors = DriveBase (left,right, 100, 156)
    middle = Motor(Port.A,Direction.CLOCKWISE,[8])
    n = 0
    while n != 4:
        Motors.drive_time(100,0,2000)
        Motors.stop(Stop.BRAKE)
        Motors.drive_time(0,45,2000)
        Motors.stop(Stop.BRAKE)
        n = n+1