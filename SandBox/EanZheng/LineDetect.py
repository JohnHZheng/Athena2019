#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import os
import sys
os.system('setfont Lat15-TerminusBold14')

lmB = LargeMotor(OUTPUT_C)
lmC = LargeMotor(OUTPUT_B)
cs1 = ColorSensor(INPUT_4)
cs4 = ColorSensor(INPUT_1)
def detect():
    times = 0
    notfoundyet = True
    while notfoundyet:
        if cs1.color == ColorSensor.COLOR_WHITE and cs4.color == ColorSensor.COLOR_WHITE:
            if cs1.reflected_light_intensity > 80 and cs4.reflected_light_intensity > 80:
                times = times+1
            if times == 2:
                notfoundyet = False
        print( "CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:04d}, CS4Reflected: {3:04d}".format( cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
            


print( "CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:04d}, CS4Reflected: {3:04d}".format( 
cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
lmB.on(60)
lmC.on(60)
detect()
lmB.off
lmC.off

#loopCounter = 0
#while (cs4.color != ColorSensor.COLOR_BLACK and cs1.color != ColorSensor.COLOR_BLACK):
""" while (loopCounter < 48):
    print( "{0:02d} - CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:04d}, CS4Reflected: {3:04d}".format( 
        loopCounter, cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
    loopCounter += 1;
    sleep(.005)

lmB.off()
lmC.off() """