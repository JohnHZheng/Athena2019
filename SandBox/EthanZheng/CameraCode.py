#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch


#Code is here
#Code is here
IR = InfraredSensor(Port.S4)
meMotor = Motor(Port.A)


while True:

    BeaconHeading = IR.beacon(4)
    #print(BeaconHeading)
    Distance, Heading = BeaconHeading
    #print(Heading)
    if Distance != None:
        Heading = Heading*15
        meMotor.run(Heading)

    

    

    
