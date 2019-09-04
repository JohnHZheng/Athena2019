#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 

class AthenaRobot(object):
    # constructors for the robot with default parameters of wheel radius and ports
    def __init__(self, wheelRadiusCm = 2.75, leftLargeMotorPort = OUTPUT_B, rightLargeMotorPort = OUTPUT_C, 
    leftMediumMotorPort = OUTPUT_A, rightMediumMotorPort = OUTPUT_D, leftSensorPort = INPUT_1, rightSensorPort = INPUT_4):
        #self is the current object, everything below for self are member variables
        self.wheelRadiusCm = wheelRadiusCm
        self.wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
        self.leftLargeMotor = LargeMotor(leftLargeMotorPort)
        self.rightLargeMotor = LargeMotor(rightLargeMotorPort) 
        self.leftMediamMotor = MediumMotor(leftMediumMotorPort)
        self.rightMediamMotor = MediumMotor(rightMediumMotorPort)
        self.leftSensor = ColorSensor(leftSensorPort)
        self.rightSensor = ColorSensor(rightSensorPort)

    # run a distance in centimeters at speed of centimeters per second
    def run(self, distanceCm, speedCmPerSecond, brake=True, block=True):
        # Calculate degrees of distances and SpeedDegreePerSecond
        degreesToRun = distanceCm / self.wheelCircumferenceCm * 360
        speedDegreePerSecond = speedCmPerSecond / self.wheelCircumferenceCm * 360
        print("Degree: {0:.3f} Speed:{1:.3f} MaxSpeed {2}".format(degreesToRun, speedDegreePerSecond, self.leftLargeMotor.max_speed), file=sys.stderr)
        # run motors based on the calculated results
        self.leftLargeMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond), degreesToRun, brake, False)
        self.rightLargeMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond), degreesToRun, brake, block)

    # turn a angle in degrees, positive means turn right and negative means turn left.
    def turn(self, degree, brake=True, block=True):
        # 1.9 is a scale factor from experiments
        degreesToRun = degree * 1.9
        # Turn at the speed of 20
        self.leftLargeMotor.on_for_degrees(20, degreesToRun, brake, False)
        self.rightLargeMotor.on_for_degrees(-20, degreesToRun, brake, block)
        
    #Medium Motor Movement
    def moveMediumMotor(self,isLeft,speed,degrees,brake=True, block=True)
        #sees which motor is running
        if isLeft == False:
            rightMediamMotor.on_for_degrees(speed,degrees,brake,block)
        else:
            leftMediamMotor.on_for_degrees(speed,degrees,brake,block)

    # run until find a game line
    def onUntilGameLine(self, consecutiveHit = 5, speed = 10, sleepTime = 0.01, white_threshold = 85, black_threshold = 30,
        brake = True):
        # Start motor at passed speed. 
        self.leftLargeMotor.on(speed)
        self.rightLargeMotor.on(speed) 

        # flags for whether both left and right wheel are in position
        leftLineSquaredWhite = False    
        rightLineSquaredWhite = False
        leftConsecutiveWhite = 0
        rightConsecutiveWhite = 0

        # first aligned on white
        while(not leftLineSquaredWhite or not rightLineSquaredWhite):
            left_reflected = self.leftSensor.reflected_light_intensity
            right_reflected = self.rightSensor.reflected_light_intensity

            # left to detect white
            if(left_reflected > white_threshold):
                leftConsecutiveWhite += 1
            else:
                leftConsecutiveWhite = 0;   # reset to zero    
            if(leftConsecutiveWhite >= consecutiveHit):
                self.leftLargeMotor.off()
                leftLineSquaredWhite = True

            # right to detect white
            if(right_reflected > white_threshold):
                rightConsecutiveWhite += 1
            else:
                rightConsecutiveWhite = 0;   # reset to zero    
            if(rightConsecutiveWhite >= consecutiveHit):
                self.rightLargeMotor.off()
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
        self.leftLargeMotor.on(speed)
        self.rightLargeMotor.on(speed) 
        while(not leftLineSquaredBlack or not rightLineSquaredBlack):
            left_reflected = self.leftSensor.reflected_light_intensity
            right_reflected = self.rightSensor.reflected_light_intensity

            # left to detect black
            if(left_reflected < black_threshold):
                leftConsecutiveBlack += 1
            else:
                leftConsecutiveBlack = 0;   # reset to zero    
            if(leftConsecutiveBlack >= consecutiveHit):
                self.leftLargeMotor.off()
                leftLineSquaredBlack = True

            # right to detect black
            if(right_reflected < black_threshold):
                rightConsecutiveBlack += 1
            else:
                rightConsecutiveBlack = 0;   # reset to zero    
            if(rightConsecutiveBlack >= consecutiveHit):
                self.rightLargeMotor.off()
                rightLineSquaredBlack = True
            print( "left_reflected: {0:3d}, right_reflected: {1:3d}, leftConsecutiveBlack: {2:3d}, rightConsecutiveBlack: {3:3d}".format( 
                left_reflected, right_reflected, leftConsecutiveBlack, rightConsecutiveBlack), file=sys.stderr)
            sleep(sleepTime) 

        self.leftLargeMotor.off()
        self.rightLargeMotor.off()
    
    #Go to the Bridge
    def goToBridge(self):
        # start from base, run 12.5 cm at 20cm/s
        self.run(12.5, 20)
        sleep(.2)
        # turn right 70 degree
        self.turn(70)
        sleep(.1)
        print("test", file=sys.stderr)
        # run 90 cm at speed of 30 cm/s
        self.run(90, 30, False)
        sleep(.1)
        # run until hit game line
        self.onUntilGameLine()
        sleep(.1)
        # move forward 2cm at 15cm/s
        self.run(2, 15)
        # turn left 90 degree
        self.turn(-90)
        # move forward 13 cm at 20cm/s
        self.run(13,20)
        sleep(.1)
        # run until hit game line
        self.onUntilGameLine()
    
    # Calibrating Color for Sensor
    def colorCalibrate(self,sensorInput):
        sensor = ColorSensor(sensorInput)
        sensor.calibrate_white()
    