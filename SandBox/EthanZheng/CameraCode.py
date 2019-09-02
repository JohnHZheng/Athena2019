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

x = 0
while x < 1000:
        BeaconHeading = IR.heading_and_distance(channel=1)
        print(BeaconHeading,file=sys.stderr)
        (Heading, Distance)= BeaconHeading
        print(Heading,file=sys.stderr)
        
        if Heading:
                print(Heading,file=sys.stderr)
                Heading = Heading*2
                meMotor.on(speed=Heading)
        else:
                meMotor.off()
        sleep(.01)
        x = x+1

        
