#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from trip1 import runTrip1
from trip2 import runTrip2
from trip3 import runTrip3
from trip4 import runTrip4

cont = True
# The master program
while cont:
    while any(brick.buttons()):
        wait(1)
    brick.display.clear()
        
    if Button.LEFT in brick.buttons():
        runTrip1()
    elif Button.UP in brick.buttons():
        runTrip2()  
    elif Button.RIGHT in brick.buttons():
        runTrip3()
    elif Button.DOWN in brick.buttons():
        runTrip4()
    elif Button.CENTER in brick.buttons():
        cont = False
    
    