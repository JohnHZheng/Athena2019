#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sound import Sound
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
import time
sound = Sound()
class AthenaRobot(object):
    # constructors for the robot with default parameters of wheel radius and ports
    def __init__(self, wheelRadiusCm = 4, leftLargeMotorPort = OUTPUT_C, rightLargeMotorPort = OUTPUT_B, 
    leftMediumMotorPort = OUTPUT_D, rightMediumMotorPort = OUTPUT_A, leftSensorPort = INPUT_4, rightSensorPort = INPUT_1):
        #self is the current object, everything below for self are member variables
        self.wheelRadiusCm = wheelRadiusCm
        self.wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
        self.leftLargeMotor = LargeMotor(leftLargeMotorPort)
        self.rightLargeMotor = LargeMotor(rightLargeMotorPort) 
        self.leftMediumMotor = MediumMotor(leftMediumMotorPort)
        self.rightMediumMotor = MediumMotor(rightMediumMotorPort)
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
    def turn(self, degree, speed = 10, brake = True , block = True):
        # 1.9 is a scale factor from experiments
        degreesToRun = degree * 1.27
        # Turn at the speed 
        self.leftLargeMotor.on_for_degrees(speed, degreesToRun, brake, False)
        self.rightLargeMotor.on_for_degrees(-speed, degreesToRun, brake, block)

    def turnOnRightWheel(self, degree, speed = 10, brake = True, block = True):
        degreesToRun = degree * 2.7
        self.rightLargeMotor.on_for_degrees(speed, degreesToRun, brake, block)

    def turnOnLeftWheel(self, degree, speed = 10, brake = True, block = True):
        degreesToRun = degree * 2.7
        self.leftLargeMotor.on_for_degrees(speed, degreesToRun, brake, block)
    #Medium Motor Movement
    def moveMediumMotor(self,isLeft,speed,degrees,brake=True, block=True):
        #sees which motor is running
        if isLeft == False:
            self.rightMediumMotor.on_for_degrees(speed,degrees,brake,block)
        else:
            self.leftMediumMotor.on_for_degrees(speed,degrees,brake,block)

    # Following a line with one sensor
    def lineFollow(self,whiteThreshold=98, blackThreshold=15, scale=0.3, useLeftSensor = True, runDistanceCM = 300, useLeftEdge = True, reverse = False):
        # Repeats when initiated
        initialPos = self.leftLargeMotor.position   # remember initial position
        loop = True
        while loop:
            reflect = self.leftSensor.reflected_light_intensity
            if useLeftSensor == False:
                reflect = self.rightSensor.reflected_light_intensity
            leftPower = abs(reflect-blackThreshold)*scale
            rightPower = abs(whiteThreshold-reflect)*scale
            # if we follow the right edge, need to swap left and right
            if useLeftEdge == False:
                oldLeft = leftPower
                leftPower = rightPower
                rightPower = oldLeft
            self.leftLargeMotor.on(leftPower)
            self.rightLargeMotor.on(rightPower)
            # Calculate the distance run in CM
            distanceRanInCM = abs((self.leftLargeMotor.position - initialPos) * (self.wheelCircumferenceCm / self.leftLargeMotor.count_per_rot))
            # Printing the reflected light intensity with the powers of the two motors
            print("reflect: {0:3d} leftPower: {1:3f} rightPower: {2:3f} lMotorPos: {3:3d} distanceRanInCM {4:3f}".format(reflect, leftPower, rightPower, 
                self.leftLargeMotor.position, distanceRanInCM), file=sys.stderr)

            if distanceRanInCM >= runDistanceCM:
                loop = False
        # Stopping the motor once the loop is over
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()

    # run until both conditions are met
    def onUntilTwoConditions(self, leftCondition, rightCondition, speed = 5, consecutiveHit = 5, sleepTime = 0.01):
         # Start motor at passed speonUntilTwoConditionsed. 
        self.leftLargeMotor.on(speed)
        self.rightLargeMotor.on(speed)    

        condLeftCounter = 0
        condRightCounter = 0
        condLeftMet = False
        condRightMet = False
     
        while(not condLeftMet or not condRightMet):
            # check left condition
            if(leftCondition()):
                condLeftCounter += 1
            else: 
                condLeftCounter = 0;    # reset to zero
            if(condLeftCounter >= consecutiveHit):
                if(condRightMet):
                    sleep(.1)
                self.leftLargeMotor.off()
                condLeftMet = True
                
            # check right condition
            if(rightCondition()):
                condRightCounter += 1
            else: 
                condRightCounter = 0;    # reset to zero
            if(condRightCounter >= consecutiveHit):
                if(condLeftMet):
                    sleep(.1)
                self.rightLargeMotor.off()
                condRightMet = True

            print( "left_reflected: {0:3d}, right_reflected: {1:3d}, leftHit: {2:3d}, rightHit: {3:3d}".format( 
                self.leftSensor.reflected_light_intensity, self.rightSensor.reflected_light_intensity, condLeftCounter, condRightCounter), file=sys.stderr)
            sleep(sleepTime) 
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()

    def onUntilWhiteLine(self, consecutiveHit = 5, speed = 5, sleepTime = 0.01, white_threshold = 85):
        self.onUntilTwoConditions(lambda : self.leftSensor.reflected_light_intensity > white_threshold, lambda : self.rightSensor.reflected_light_intensity > white_threshold, 
            speed, consecutiveHit, sleepTime)

    def onUntilBlackLine(self, consecutiveHit = 5, speed = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilTwoConditions(lambda : self.leftSensor.reflected_light_intensity < black_threshold, lambda : self.rightSensor.reflected_light_intensity < black_threshold, 
            speed, consecutiveHit, sleepTime)        

    # run until find a game line
    def onUntilGameLine(self, consecutiveHit = 5, speed = 5, sleepTime = 0.01, white_threshold = 85, black_threshold = 30):
        self.onUntilWhiteLine(consecutiveHit, speed, sleepTime, white_threshold)
        self.onUntilBlackLine(consecutiveHit, speed, sleepTime, black_threshold)

    # run until condition is met
    def onUntilCondition(self, condition, speed = 5, consecutiveHit = 5, sleepTime = 0.01):
         # Start motor at passed speonUntilTwoConditionsed. 
        self.leftLargeMotor.on(speed)
        self.rightLargeMotor.on(speed)    
        counter = 0
        condMet = False
     
        while(not condMet):
            # check condition
            if(condition()):
                counter += 1
            else: 
                counter = 0;    # reset to zero
            if(counter >= consecutiveHit):
                self.leftLargeMotor.off()
                self.rightLargeMotor.off()
                condMet = True
                
            print( "left_reflected: {0:3d}, right_reflected: {1:3d}, hit: {2:3d}".format( 
                self.leftSensor.reflected_light_intensity, self.rightSensor.reflected_light_intensity, counter), file=sys.stderr)
            sleep(sleepTime) 
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()

    def onUntilLeftBlack(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity < black_threshold, speed, consecutiveHit, sleepTime)
    def onUntilLeftWhite(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, white_threshold = 85):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity > white_threshold, speed, consecutiveHit, sleepTime)
    def onUntilRightBlack(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity < black_threshold, speed, consecutiveHit, sleepTime)
    def onUntilLeftWhite(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, white_threshold = 85):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity > white_threshold, speed, consecutiveHit, sleepTime)

    #Go to the Bridge
    def goToBridge(self):
        # start from base, run 12.5 cm at 20cm/s
        self.run(10, 20)
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
    
    # Calibrating White for Sensor
    def calibrateColorSensor(self,sensorInput):
        sensor = ColorSensor(sensorInput)
        # Calibration
        sensor.calibrate_white()
    
        # Done Signal
        sound.beep()

    # Calibrating Color for Sensor
    def testColorSensor(self,sensorInput,sensorPort,repeatNumber = 10,pauseNumber = 0.2, speed = 0):
        sensor = ColorSensor(sensorInput)
        if(speed > 0 ):
            self.leftLargeMotor.on(speed)
            self.rightLargeMotor.on(speed)              
        times = 0
        # For loop
        while times != repeatNumber:
            # Print
            print("Sensor {0:3d}: {1:3d}".format(sensorPort, sensor.reflected_light_intensity), file=sys.stderr)
            time.sleep(pauseNumber)
            times = times + 1
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()       

    def testRobot(self):
        # self.leftLargeMotor.on_for_degrees( 20, 360, True , True)
        # sleep(1)
        # self.rightLargeMotor.on_for_degrees( 20, 360, True , True)
        # self.turn(90)
        # sleep(1)
        # self.turnOnLeftWheel(90)
        # sleep(1)
        # self.turnOnRightWheel(90)
        # sleep(1)
        self.moveMediumMotor(True,10,360) 
        sleep(1)
        self.moveMediumMotor(False,10,360)
        sleep(1)
