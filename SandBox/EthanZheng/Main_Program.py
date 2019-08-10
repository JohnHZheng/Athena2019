#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from Mission1 import stuff

while True:
    stuff()
    while any(brick.buttons()):
        wait(1)
    brick.display.clear()
        
    if Button.LEFT in brick.buttons():
        brick.display.text("First Program",(60,50))
    elif Button.UP in brick.buttons():
        brick.display.text("Second Program", (60,50))       
    elif Button.RIGHT in brick.buttons():
        brick.display.text("Third Program", (60,50))
    elif Button.DOWN in brick.buttons():
        brick.display.text("Fourth Program", (60,50))
    elif Button.CENTER in brick.buttons():
        brick.display.text("Fifth Program", (60,50))
    
    