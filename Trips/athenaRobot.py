#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sound import Sound
from time import sleep
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
import time
sound = Sound()
class AthenaRobot(object):
    # constructors for the robot with default parameters of wheel radius and ports
    def __init__(self, wheelRadiusCm = 4, leftLargeMotorPort = OUTPUT_B, rightLargeMotorPort = OUTPUT_C, 
    leftMediumMotorPort = OUTPUT_A, rightMediumMotorPort = OUTPUT_D, leftSensorPort = INPUT_1, rightSensorPort = INPUT_4, ultraSonicSensorPort = INPUT_2):
        #self is the current object, everything below for self are member variables
        self.wheelRadiusCm = wheelRadiusCm
        self.wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
        self.leftLargeMotor = LargeMotor(leftLargeMotorPort)
        self.rightLargeMotor = LargeMotor(rightLargeMotorPort) 
        self.leftMediumMotor = MediumMotor(leftMediumMotorPort)
        self.rightMediumMotor = MediumMotor(rightMediumMotorPort)
        self.leftSensor = ColorSensor(leftSensorPort)
        self.rightSensor = ColorSensor(rightSensorPort)
        self.ultraSonicSensor = UltrasonicSensor(ultraSonicSensorPort) 
        

    # run a distance in centimeters at speed of centimeters per second
    def run(self, distanceCm, speedCmPerSecond, brake=True, block=True):
        if speedCmPerSecond < 0:
            raise Exception('speed cannot be negative')
        # Calculate degrees of distances and SpeedDegreePerSecond
        degreesToRun = distanceCm / self.wheelCircumferenceCm * 360
        speedDegreePerSecond = speedCmPerSecond / self.wheelCircumferenceCm * 360
        print("Run - Degree: {0:.3f} Speed:{1:.3f} MaxSpeed {2}".format(degreesToRun, speedDegreePerSecond, self.leftLargeMotor.max_speed), file=sys.stderr)
        # run motors based on the calculated results
        self.leftLargeMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond) * (-1), degreesToRun, brake, False)
        self.rightLargeMotor.on_for_degrees(SpeedDPS(speedDegreePerSecond) * (-1) , degreesToRun, brake, block)

    # turn a angle in degrees, positive means turn right and negative means turn left.
    def turn(self, degree, speed = 10, brake = True , block = True):
        # 1.9 is a scale factor from experiments
        degreesToRun = degree * 1.275
        # Turn at the speed 
        self.leftLargeMotor.on_for_degrees(-speed, degreesToRun, brake, False)
        self.rightLargeMotor.on_for_degrees(speed, degreesToRun, brake, block)

    def turnOnRightWheel(self, degree, speed = 10, brake = True, block = True):
        degreesToRun = degree * 2.7
        self.rightLargeMotor.on_for_degrees(-speed, degreesToRun, brake, block)

    def turnOnLeftWheel(self, degree, speed = 10, brake = True, block = True):
        degreesToRun = degree * 2.7
        self.leftLargeMotor.on_for_degrees(-speed, degreesToRun, brake, block)
    #Medium Motor Movement 
    def moveMediumMotor(self,isLeft,speed,degrees,brake=True, block=True):
        #sees which motor is running
        if isLeft == False:
            self.rightMediumMotor.on_for_degrees(speed,degrees,brake,block)
        else:
            self.leftMediumMotor.on_for_degrees(speed,degrees,brake,block)

    # Following a line with one sensor
    def lineFollow(self, whiteThreshold = 98, blackThreshold = 15, scale=0.2, useLeftSensor = True, useLeftEdge = True, runDistanceCM = 300, ):
        self.leftLargeMotor.reset()
        self.rightLargeMotor.reset()
        # Allow an attached backsensor. Ixf useBackSensor, defining back sensor and revert useLeftEdge since motor is actually going backward
        initialPos = self.leftLargeMotor.position   # remember initial position
        loop = True
        while loop:
            # use left or right sensor based on passed in useLeftSensor
            reflect = self.leftSensor.reflected_light_intensity if useLeftSensor == True else self.rightSensor.reflected_light_intensity
            # Allow an attached backsensor. If useBackSensor, use reflected_light_intensity of that sensor

            leftPower = abs(reflect-blackThreshold) * scale
            rightPower = abs(whiteThreshold-reflect) * scale
            # if we follow the right edge, need to swap left and right
            if useLeftEdge == False:
                oldLeft = leftPower
                leftPower = rightPower
                rightPower = oldLeft
            self.leftLargeMotor.on(-leftPower)
            self.rightLargeMotor.on(-rightPower)
            # Calculate the distance run in CM
            distanceRanInCM = abs((self.leftLargeMotor.position - initialPos) * (self.wheelCircumferenceCm / self.leftLargeMotor.count_per_rot))
            # Printing the reflected light intensity with the powers of the two motors
            print("LineFollow - reflect: {0:3d} leftPower: {1:3f} rightPower: {2:3f} lMotorPos: {3:3d} distanceRanInCM {4:3f}".format(reflect, leftPower, rightPower, 
                self.leftLargeMotor.position, distanceRanInCM), file=sys.stderr)

            if distanceRanInCM >= runDistanceCM:
                loop = False
        # Stopping the motor once the loop is over
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()

    # run until both conditions are met
    def onUntilTwoConditions(self, leftCondition, rightCondition, caller, speed = 5, consecutiveHit = 5, sleepTime = 0.01):
         # Start motor at passed speonUntilTwoConditionsed. 
        self.leftLargeMotor.on(-speed)
        self.rightLargeMotor.on(-speed)    

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

            print( "{4}-onUntilTwoConditions: left_reflected: {0:3d}, right_reflected: {1:3d}, leftHit: {2:3d}, rightHit: {3:3d}".format( 
                self.leftSensor.reflected_light_intensity, self.rightSensor.reflected_light_intensity, condLeftCounter, condRightCounter, caller), file=sys.stderr)
            sleep(sleepTime) 
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()

    def onUntilWhiteLine(self, consecutiveHit = 5, speed = 5, sleepTime = 0.01, white_threshold = 85):
        self.onUntilTwoConditions(lambda : self.leftSensor.reflected_light_intensity > white_threshold, lambda : self.rightSensor.reflected_light_intensity > white_threshold, 
            "onUntilWhiteLine", speed, consecutiveHit, sleepTime)

    def onUntilBlackLine(self, consecutiveHit = 5, speed = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilTwoConditions(lambda : self.leftSensor.reflected_light_intensity < black_threshold, lambda : self.rightSensor.reflected_light_intensity < black_threshold, 
            "onUntilBlackLine", speed, consecutiveHit, sleepTime)        

    # run until find a game line
    def onUntilGameLine(self, consecutiveHit = 5, speed = 5, sleepTime = 0.01, white_threshold = 85, black_threshold = 30):
        self.onUntilWhiteLine(consecutiveHit, speed, sleepTime, white_threshold)
        self.onUntilBlackLine(consecutiveHit, speed, sleepTime, black_threshold)

    # run until condition is met
    def onUntilCondition(self, condition, caller, leftSpeed = 5, rightSpeed = 5, consecutiveHit = 5, sleepTime = 0.01, revert = False):
        # Start motor at passed speonUntilTwoConditionsed. 
        self.leftLargeMotor.on(-leftSpeed if revert == False else leftSpeed)
        self.rightLargeMotor.on(-rightSpeed if revert == False else rightSpeed)    
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
                
            print( "{4}-onUntilCondition: ColorSensor(left_reflected: {0:3d}, right_reflected: {1:3d}, hit: {2:3d}), UltraSonicSensor(distance_centimeters: {3:3f})".format( 
                self.leftSensor.reflected_light_intensity, self.rightSensor.reflected_light_intensity, counter, self.ultraSonicSensor.distance_centimeters, caller), file=sys.stderr)
            sleep(sleepTime) 
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()

    def onUntilLeftBlack(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity < black_threshold, "onUntilLeftBlack",
        speed, speed, consecutiveHit, sleepTime)
    def onUntilLeftWhite(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, white_threshold = 85):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity > white_threshold, "onUntilLeftWhite",
        speed, speed, consecutiveHit, sleepTime)
    def onUntilRightBlack(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity < black_threshold, "onUntilRightBlack",
        speed, speed, consecutiveHit, sleepTime)
    def onUntilRightWhite(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, white_threshold = 85):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity > white_threshold, "onUntilRightWhite",
        speed, speed, consecutiveHit, sleepTime)

    def turnUntilLeftBlack(self, turnLeft,speed, consecutiveHit = 2,  black_threshold = 30):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity < black_threshold, "turnUntilLeftBlack",
            0 if turnLeft == True else speed, speed if turnLeft == True else 0, consecutiveHit)
    def turnUntilLeftWhite(self, turnLeft,speed, consecutiveHit = 2,  white_threshold = 85):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity > white_threshold, "turnUntilLeftWhite",
            0 if turnLeft == True else speed, speed if turnLeft == True else 0, consecutiveHit)
    def turnUntilRightBlack(self, turnLeft,speed, consecutiveHit = 2,  black_threshold = 30):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity < black_threshold, "turnUntilRightBlack",
            0 if turnLeft == True else speed, speed if turnLeft == True else 0, consecutiveHit)
    def turnUntilRightWhite(self, turnLeft,speed, consecutiveHit = 2,  white_threshold = 85):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity > white_threshold, "turnUntilRightWhite",
            0 if turnLeft == True else speed, speed if turnLeft == True else 0, consecutiveHit)

    # Go until sensor reading has a specified offset or reach to the threshhold
    def onUntilRightDarkerBy(self, difference, black_threshold = 20, speed = 10, consecutiveHit = 2):
        originalValue = self.rightSensor.reflected_light_intensity
        print( "onUntilRightDarkerBy - originalValue: {0:3d}, diff: {1:3d}".format(originalValue, difference), file=sys.stderr)
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity - originalValue < -difference or self.rightSensor.reflected_light_intensity < black_threshold, "onUntilRightSensorDiff", consecutiveHit=consecutiveHit) 
    def onUntilRightLighterBy(self, difference, white_threshold = 80, speed = 10, consecutiveHit = 2):
        originalValue = self.rightSensor.reflected_light_intensity
        print( "onUntilRightLighterBy - originalValue: {0:3d}, diff: {1:3d}".format(originalValue, difference), file=sys.stderr)
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity - originalValue > difference or self.rightSensor.reflected_light_intensity > white_threshold, "onUntilRightSensorDiff", consecutiveHit=consecutiveHit) 

    #uses Ultrasonic sensor to see wall as going back
    def revertSafely(self,speed=100,distanceToStop=10,consecutiveHit=1,sleepTime=0.01):
        self.onUntilCondition(lambda : self.ultraSonicSensor.distance_centimeters < distanceToStop, "revertSafely", speed, speed, consecutiveHit, sleepTime, True)

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
            print("testColorSensor- Port: {0:3d}: {1:3d}".format(sensorPort, sensor.reflected_light_intensity), file=sys.stderr)
            time.sleep(pauseNumber)
            times = times + 1
        self.leftLargeMotor.off()
        self.rightLargeMotor.off()       

    def testRobot(self):
        self.leftLargeMotor.on_for_degrees(20,180)
        sleep(.1)
        self.rightLargeMotor.on_for_degrees(20,180)
        sleep(.1)
        self.moveMediumMotor(True,10,180)
        sleep(.1)
        self.moveMediumMotor(False,10,180)
        sleep(.1)
        self.run(20, 10) 
        sleep(.1)
        self.run(-20, 10) 
        sleep(.1)        
        self.turn(90)
        sleep(.1)
        self.turn(-90)
        sleep(.1)
        self.turnOnLeftWheel(90)
        sleep(.1)
        self.turnOnLeftWheel(-90)
        sleep(.1)
        self.turnOnRightWheel(90)
        sleep(.1)
        self.turnOnRightWheel(-90)
        sleep(.1)
        self.calibrateColorSensor(INPUT_1)
        self.calibrateColorSensor(INPUT_4)
        self.testColorSensor(INPUT_1, 1)
        self.testColorSensor(INPUT_4, 4)               

