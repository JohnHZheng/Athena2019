#!/usr/bin/env micropython

from ev3dev2.motor import MediumMotor, OUTPUT_A
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from time import sleep
import math
import sys

#Code is here
IR = InfraredSensor(INPUT_4)
meMotor = MediumMotor(OUTPUT_A)


for x in range(1000):
    BeaconHeading = IR.heading_and_distance(channel=4)
    print(BeaconHeading,file=sys.stderr)
    (Distance, Heading)= BeaconHeading
    print(Heading,file=sys.stderr)
    sleep(.01)
    if Distance:
        print(Heading,file=sys.stderr)
        Heading = Heading*15
        meMotor.on(speed=Heading)
        
