#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
#Creating Motors
leftWheel = Motor(Port.B)
rightWheel = Motor(Port.C)
example_motor = Motor(Port.A)
# MoveForward Function
def MoveForward(Speed,Degree):
    for x in range(0,Degree):
        rightWheel.run_target(Speed,1,)
        leftWheel.run_target(Speed,1)
#Turning
example_motor.run_target(500,360,Stop.BRAKE)
#Drive Base
robot = DriveBase(leftWheel,rightWheel,100,160)