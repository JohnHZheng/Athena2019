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

def run(distanceCm, speedCmPerSecond, leftMotorPort = OUTPUT_B, rightMotorPort = OUTPUT_C, brake=True, block=True):
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
run(50, 30)
sleep(0.2)
# run backward 50 cm at speed of 20cm/s
run(-50, 20)

def onUntilGameLine( white_threshold = 85, black_threshold = 30,
    leftMotorPort = OUTPUT_B, rightMotorPort = OUTPUT_C, leftSensorPort = INPUT_1, rightSensorPort = INPUT_4, brake = True):
    # Initialize Motors and sensors
    leftMotor = LargeMotor(leftMotorPort)
    rightMotor = LargeMotor(rightMotorPort) 
    leftSensor = ColorSensor(leftSensorPort)
    rightSensor = ColorSensor(rightSensorPort)

    # calculate speed to use in DPS
    speedDegreePerSecond = speedCmPerSecond / wheelCircumferenceCm * 360

    # Start motor at internal determined speed. 
    leftMotor.on(15)
    rightMotor.on(15) 

    # flags for whether both left and right wheel are in position
    leftStopped = False
    rightStopped = False

    while(not leftStopped or not rightStopped):
        left_reflected = leftSensor.reflected_light_intensity
        right_reflected = leftSensor.reflected_light_intensity
        sleep(.005) 

    #while (cs4.color != ColorSensor.COLOR_BLACK and cs1.color != ColorSensor.COLOR_BLACK):
    """
     while (loopCounter < 24):
        print( "{0:02d} - CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:04d}, CS4Reflected: {3:04d}".format( 
            loopCounter, cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
        loopCounter += 1;
        sleep(.005) 
    """

    leftMotor.off()
    rightMotor.off()




