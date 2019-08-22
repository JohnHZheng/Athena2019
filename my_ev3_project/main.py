#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
left = Motor(Port.B)
right = Motor(Port.C)

n = 0
while n<=3:
    left.run_time(-500,2000, Stop.COAST, False)
    right.run_time(-500,2000,Stop.COAST)
    left.run_angle(360,-320,Stop.BRAKE, True)
    n=n+1



