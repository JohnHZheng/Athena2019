#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

left =  Motor(Port.C)
right = Motor(Port.B)
Motors = DriveBase (left,right, 100, 156)
leftS = ColorSensor (Port.S4)
rightS = ColorSensor (Port.S1)

def LineFollow():
    while True:
        if leftS.color() == 6:
            if rightS.color() == 6:
                Motors.drive(150,0)
            elif rightS.color != 6:
                left.stop()
                right.run(75) 
        elif rightS.color() == 1:
            right.stop()
            left.run(75)
        elif leftS.color() == 1:
            left.stop()
            right.run(75)  
            
        elif leftS.color != 6:
            right.stop()
            left.run(75)   
LineFollow()