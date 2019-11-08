#!/usr/bin/env micropython
afrom ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent

class AthenaRobot(object):
    # constructors for the robot with default parameters of wheel radius and ports
    def __init__(self, wheelRadiusCm = 4, leftLargeMotorPort = OUTPUT_B, rightLargeMotorPort = OUTPUT_C, 
    leftMediumMotorPort = OUTPUT_A, rightMediumMotorPort = OUTPUT_D, leftSensorPort = INPUT_1, rightSensorPort = INPUT_4, ultraSonicSensorPort = INPUT_2):
        ...
    
    def turn(self, degree, speed = 10, brake = True , block = True):
        ...
    def onUntilCondition(self, condition, caller, leftSpeed = 5, rightSpeed = 5, consecutiveHit = 5, sleepTime = 0.01, revert = False):
        ...
    def lineFollow(self, whiteThreshold = 98, blackThreshold = 15, scale=0.2, useLeftSensor = True, useLeftEdge = True, runDistanceCM = 300, ):
        ...
    def run(self, distanceCm, speedCmPerSecond, brake=True, block=True):
        ...
    def onUntilLeftBlack(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity < black_threshold, "onUntilLeftBlack",
        speed, speed, consecutiveHit, sleepTime)

    def turnUntilRightWhite(self, turnLeft,speed, consecutiveHit = 2,  white_threshold = 85):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity > white_threshold, "turnUntilRightWhite",
        0 if turnLeft == True else speed, speed if turnLeft == True else 0, consecutiveHit)

Slide 2: FUnction problem that utilize the lower level function

    def turnRight(self, degree, speed = 10, brake = True , block = True):
    self.turn(degree, speed, brake, block)
    #lambada functions

    # Turns until the right color sensor detects white
    def turnUntilRightWhite(self, turnLeft,speed, consecutiveHit = 2,  white_threshold = 85):
        self.onUntilCondition(lambda : self.rightSensor.reflected_light_intensity > white_threshold, "turnUntilRightWhite",
        0 if turnLeft == True else speed, speed if turnLeft == True else 0, consecutiveHit)
    # Goes forward until left color sensor detects black
    def onUntilLeftBlack(self, speed = 5, consecutiveHit = 5, sleepTime = 0.01, black_threshold = 30):
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity < black_threshold, "onUntilLeftBlack", speed, speed, consecutiveHit, sleepTime)

    # Uses Ultrasonic sensor to see wall as going back
    def revertSafely(self,speed=100,distanceToStop=10,consecutiveHit=1,sleepTime=0.01):
        self.onUntilConditionx(lambda : self.ultraSonicSensor.distance_centimeters < distanceToStop, "revertSafely", speed, speed, consecutiveHit, sleepTime, True)

    # Goes forward until left sensor's light reflected intensity increases
    def onUntilLeftLighterBy(self, difference, white_threshold = 80, speed = 10, consecutiveHit = 2):
        originalValue = self.leftSensor.reflected_light_intensity
        print( "onUntilLeftLighterBy - originalValue: {0:3d}, diff: {1:3d}".format(originalValue, difference), file=sys.stderr)
        self.onUntilCondition(lambda : self.leftSensor.reflected_light_intensity - originalValue > difference or self.leftSensor.reflected_light_intensity > white_threshold, 
        "onUntilLeftSensorDiff", consecutiveHit=consecutiveHit) 

Slide 3: Trip 1 where we use our functions

    robot = AthenaRobot()

    robot.run(distanceCm = 34, speedCmPerSecond = 15, brake = False) 
    robot.lineFollow(useLeftSensor = False, useLeftEdge = True, runDistanceCM = 17, scale=.18)
    robot.onUntilRightLighterBy(difference = 20 , white_threshold= white_value_right)
    robot.turnLeftOnRightWheel(degree = 60, speed = 10)
    robot.moveMediumMotor(isLeft = False, speed = mediumMotorDownSpeed, degrees = mediumMotorDownDegrees)
    robot.onUntilBlackLine(consecutiveHit = 1, speed = -10, black_threshold = black_value)
    robot.onUntilWhiteLine(consecutiveHit = 1, speed = 10, white_threshold = 75)
    ...

Slide 4:  Diagnosis tracing information

print( "{4}-onUntilCondition: ColorSensor(left_reflected: {0:3d}, right_reflected: {1:3d}, hit: {2:3d}), UltraSonicSensor(distance_centimeters: {3:3f})".format( 
self.leftSensor.reflected_light_intensity, self.rightSensor.reflected_light_intensity, counter, 
self.ultraSonicSensor.distance_centimeters, caller), file=sys.stderr)
#Tracing Information
onUntilLeftWhite-onUntilCondition: ColorSensor(left_reflected:  11, right_reflected:   8, hit:   0), UltraSonicSensor(distance_centimeters: 18.300000)
onUntilWhiteLine-onUntilTwoConditions: left_reflected:  86, right_reflected:  71, leftHit:   8, rightHit:   0
LineFollow - reflect:  10 leftPower: 10.560000 rightPower: 0.600000 lMotorPos: -197 distanceRanInCM 13.753195
Run - Degree: 343.775 Speed:286.479 MaxSpeed 1050
onUntilRightSensorDiff-onUntilCondition: ColorSensor(left_reflected:  21, right_reflected:  38, hit:   0), UltraSonicSensor(distance_centimeters: 49.000000)
revertSafely-onUntilCondition: ColorSensor(left_reflected:   3, right_reflected:   3, hit:   0), UltraSonicSensor(distance_centimeters: 11.200000)