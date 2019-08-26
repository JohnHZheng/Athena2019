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

def run(distanceCm, speedCmPerSecond, leftMotorPort = OUTPUT_C, rightMotorPort = OUTPUT_B, brake=True, block=True):
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

def onUntilGameLine( consecutiveHit = 3, speed = 15, sleepTime = 0.01, white_threshold = 90, black_threshold = 30,
    leftMotorPort = OUTPUT_C, rightMotorPort = OUTPUT_B, leftSensorPort = INPUT_4, rightSensorPort = INPUT_1, brake = True):
    # Initialize Motors and sensors
    leftMotor = LargeMotor(leftMotorPort)
    rightMotor = LargeMotor(rightMotorPort) 
    leftSensor = ColorSensor(leftSensorPort)
    rightSensor = ColorSensor(rightSensorPort)

    # Start motor at passed speed. 
    leftMotor.on(speed)
    rightMotor.on(speed) 

    # flags for whether both left and right wheel are in position
    leftLineSquaredWhite = False    
    rightLineSquaredWhite = False
    leftConsecutiveWhite = 0
    rightConsecutiveWhite = 0

    # first aligned on white
    while(not leftLineSquaredWhite or not rightLineSquaredWhite):
        left_reflected = leftSensor.reflected_light_intensity
        right_reflected = rightSensor.reflected_light_intensity

        # left to detect white
        if(left_reflected > white_threshold):
            leftConsecutiveWhite += 1
        else:
            leftConsecutiveWhite = 0;   # reset to zero    
        if(leftConsecutiveWhite >= consecutiveHit):
            leftMotor.off()
            leftLineSquaredWhite = True

        # right to detect white
        if(right_reflected > white_threshold):
            rightConsecutiveWhite += 1
        else:
            rightConsecutiveWhite = 0;   # reset to zero    
        if(rightConsecutiveWhite >= consecutiveHit):
            rightMotor.off()
            rightLineSquaredWhite = True
        print( "left_reflected: {0:3d}, right_reflected: {1:3d}, leftConsecutiveWhite: {2:3d}, rightConsecutiveWhite: {3:3d}".format( 
            left_reflected, right_reflected, leftConsecutiveWhite, rightConsecutiveWhite), file=sys.stderr)
        sleep(sleepTime) 

    print("*********** White Line Reached *********", file=sys.stderr)

    leftLineSquaredBlack = False    
    rightLineSquaredBlack = False
    leftConsecutiveBlack = 0
    rightConsecutiveBlack = 0

    # now try black
    leftMotor.on(speed)
    rightMotor.on(speed) 
    while(not leftLineSquaredBlack or not rightLineSquaredBlack):
        left_reflected = leftSensor.reflected_light_intensity
        right_reflected = rightSensor.reflected_light_intensity

        # left to detect black
        if(left_reflected < black_threshold):
            leftConsecutiveBlack += 1
        else:
            leftConsecutiveBlack = 0;   # reset to zero    
        if(leftConsecutiveBlack >= consecutiveHit):
            leftMotor.off()
            leftLineSquaredBlack = True

        # right to detect black
        if(right_reflected < black_threshold):
            rightConsecutiveBlack += 1
        else:
            rightConsecutiveBlack = 0;   # reset to zero    
        if(rightConsecutiveBlack >= consecutiveHit):
            rightMotor.off()
            rightLineSquaredBlack = True
        print( "left_reflected: {0:3d}, right_reflected: {1:3d}, leftConsecutiveBlack: {2:3d}, rightConsecutiveBlack: {3:3d}".format( 
            left_reflected, right_reflected, leftConsecutiveBlack, rightConsecutiveBlack), file=sys.stderr)
        sleep(sleepTime) 
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

# run forward 50 cm at speed of 30cm/s
# run(50, 30)
# sleep(0.2)
# run backward 50 cm at speed of 20cm/s
# run(-50, 20)

# run(3, 30, brake=False)

onUntilGameLine(consecutiveHit = 5, white_threshold=65, black_threshold=30, speed=10)


