#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

CS = ColorSensor(Port.S4)
def ColorSense():

    if CS.color() == 1:
        brick.display.text("Black",(60,50))
    elif CS.color() == 2:
        brick.display.text("Blue",(60,50))
    elif CS.color() == 3:
        brick.display.text("Green",(60,50))
    elif CS.color() == 4:
        brick.display.text("Yellow",(60,50))
    elif CS.color() == 5:
        brick.display.text("Red",(60,50))
    elif CS.color() == 6:
        brick.display.text("White",(60,50))
    elif CS.color() == 7:
        brick.display.text("Brown",(60,50))
    else:
        brick.display.text("None", (60,50))
    wait(1000)
    brick.display.clear()