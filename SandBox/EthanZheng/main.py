#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from Mission1 import Dance
from Mission2 import Square
from Mission3 import ColorSense
from Mission4 import Circle

while True:
    
    while any(brick.buttons()):
        wait(1)
    brick.display.clear()
        
    if Button.LEFT in brick.buttons():
        Dance()
    elif Button.UP in brick.buttons():
        Square()  
    elif Button.RIGHT in brick.buttons():
        ColorSense()
    elif Button.DOWN in brick.buttons():
        Circle()
    elif Button.CENTER in brick.buttons():
        brick.display.text("Fifth Program", (60,50))
    
    