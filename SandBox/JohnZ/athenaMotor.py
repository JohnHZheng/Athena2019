#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 

# wheel constances in Center Meter
wheelRadiusCm = 2.75 
wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm

def Run(distanceCm, speedCmPerSecond, leftMotorPort = OUTPUT_B, rightMotorPort = OUTPUT_C, brake=True, block=True):
    # Initialize Motors
    leftMotor = LargeMotor(leftMotorPort)
    rightMotor = LargeMotor(rightMotorPort)  
    # Calculate degrees of distances and SpeedDegreePerSecond
    degreesToRun = distanceCm / wheelCircumferenceCm * 360
    speedDegreePerSecond = speedCmPerSecond / wheelCircumferenceCm * 360
    print("Degree: {0:.3f} Speed:{1:.3f} MaxSpeed {2}".format(degreesToRun, speedDegreePerSecond, leftMotor.max_speed), file=sys.stderr)
    # run motors based on the calculated results
    leftMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond), degreesToRun, brake, False)
    rightMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond), degreesToRun, brake, block)

# run forward 50 cm at speed of 30cm/s
Run(50, 30)
sleep(0.2)
# run backward 50 cm at speed of 20cm/s
Run(-50, 20)