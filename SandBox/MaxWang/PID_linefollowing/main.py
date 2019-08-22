#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
LeftWheel   = Motor(Port.B, Direction.COUNTERCLOCKWISE)
RightWheel  = Motor(Port.C, Direction.COUNTERCLOCKWISE)
Sensor1     = ColorSensor(Port.S1)
Sensor2     = ColorSensor(Port.S4)
Kp          = 4
Target      = 50
SumAngle    = 0
NowAngle    = LeftWheel.angle()
Distance    = 750
while SumAngle < Distance :
    SensorReading   = Sensor2.reflection() 
    Err             = SensorReading - Target
    DeltaS          = Kp * Err
    LeftWheel.run(500 - DeltaS)
    RightWheel.run(500 + DeltaS)
    LastAngle       = NowAngle
    NowAngle        = LeftWheel.angle()
    DeltaAngle      = NowAngle - LastAngle
    if DeltaAngle < 0:
        DeltaAngle = DeltaAngle + 360
    SumAngle       = SumAngle + DeltaAngle
LeftWheel.stop(Stop.BRAKE)
RightWheel.stop(Stop.BRAKE)


 









