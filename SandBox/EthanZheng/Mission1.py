#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
leftWheel = Motor(Port.B)
rightWheel = Motor(Port.C)
def Dance():
        x=0
        for x in range(5):
                brick.light(Color.RED)
                brick.display.text("Go Athena!!!",(50,60))
                leftWheel.run_target(3000,360,Stop.BRAKE)
                brick.light(Color.YELLOW)
                leftWheel.run_target(3000,-360,Stop.BRAKE)
                brick.light(Color.ORANGE)
                
                
        brick.sound.file(SoundFile.CHEERING)