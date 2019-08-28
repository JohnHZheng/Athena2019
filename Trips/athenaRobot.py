#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 

class AthenaRobot(object):
    # constructors for the robot with default parameters of wheel radius and ports
    def __init__(self, wheelRadiusCm = 2.75, leftMotorPort = OUTPUT_C, rightMotorPort = OUTPUT_B, leftSensorPort = INPUT_4, rightSensorPort = INPUT_1):
        #self is the current object, everything below for self are member variables
        self.wheelRadiusCm = wheelRadiusCm
        self.wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
        self.leftMotor = LargeMotor(leftMotorPort)
        self.rightMotor = LargeMotor(rightMotorPort) 
        self.leftSensor = ColorSensor(leftSensorPort)
        self.rightSensor = ColorSensor(rightSensorPort)

    # run a distance in centimeters at speed of centimeters per second
    def run(self, distanceCm, speedCmPerSecond, brake=True, block=True):
        # Calculate degrees of distances and SpeedDegreePerSecond
        degreesToRun = distanceCm / self.wheelCircumferenceCm * 360
        speedDegreePerSecond = speedCmPerSecond / self.wheelCircumferenceCm * 360
        print("Degree: {0:.3f} Speed:{1:.3f} MaxSpeed {2}".format(degreesToRun, speedDegreePerSecond, self.leftMotor.max_speed), file=sys.stderr)
        # run motors based on the calculated results
        self.leftMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond), degreesToRun, brake, False)
        self.rightMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond), degreesToRun, brake, block)

    # turn a angle in degrees, positive means turn right and negative means turn left.
    def turn(self, degree, brake=True, block=True):
        # 1.9 is a scale factor from experiments
        degreesToRun = degree * 1.9
        # Turn at the speed of 20
        self.leftMotor.on_for_degrees(20, degreesToRun, brake, False)
        self.rightMotor.on_for_degrees(-20, degreesToRun, brake, block)