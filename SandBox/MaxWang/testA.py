#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,MediumMotor, OUTPUT_D, OUTPUT_A,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sound import Sound
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
import math
import sys 
import time
LeftAction      = MediumMotor(OUTPUT_A)
RightAction     = MediumMotor(OUTPUT_D)
TankPair        = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
LeftSensor      = ColorSensor(INPUT_1)
RightSensor     = ColorSensor(INPUT_4)
LeftWheel       = LargeMotor(OUTPUT_B)
RightWheel      = LargeMotor(OUTPUT_C)
sound           = Sound()


def Step1():
    TankPair.on_for_seconds(SpeedDPS(450),SpeedDPS(455), 1.3,False,True)
    TankPair.on_for_seconds(SpeedDPS(345),SpeedDPS(350), 1,False,True)

def Step2():   
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 250,True,True)
    TankPair.on_for_seconds(SpeedDPS(400),SpeedDPS(0), 0.5,True,True)
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(250),SpeedDPS(250))
    LeftWheel.off()
    RightWheel.off()
    while LeftSensor.color != 6:
        TankPair.on(SpeedDPS(250),SpeedDPS(250))
    LeftWheel.off()
    RightWheel.off()
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 20,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(350), 250,True,True)   
    

def LineFollowing(FastSpeed,SlowSpeed,Degree):
    DegreeSum = 0
    AngleOld    = 360 * LeftWheel.position / LeftWheel.count_per_rot
    while DegreeSum < Degree:
        if LeftSensor.color == ColorSensor.COLOR_WHITE:
            RightWheel.on(SpeedDPS(FastSpeed))
            LeftWheel.on(SpeedDPS(SlowSpeed))
        else:
            LeftWheel.on(SpeedDPS(FastSpeed))
            RightWheel.on(SpeedDPS(SlowSpeed))  
        #print("LeftSensor - color:{0}", LeftSensor.color_name, file=sys.stderr)
        AngleNew    = 360 * LeftWheel.position / LeftWheel.count_per_rot
        DegreeSum   = DegreeSum + AngleNew - AngleOld
        AngleOld    = AngleNew
    LeftWheel.off()
    RightWheel.off()  
def Step3():  
    LineFollowing(200,70,400)
    TankPair.on_for_degrees(SpeedDPS(300), SpeedDPS(300),350,True,True )
    LineFollowing(150,40,350)
    TankPair.on_for_degrees(SpeedDPS(-200), SpeedDPS(200),100,True,True )
    TankPair.on_for_degrees(SpeedDPS(300), SpeedDPS(300),120,True,True )

def Step4():
    TankPair.on_for_degrees(SpeedDPS(-300), SpeedDPS(-300),200,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250), SpeedDPS(0),380,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250), SpeedDPS(-250),475,True,True)
    TankPair.on_for_degrees(SpeedDPS(250), SpeedDPS(0),150,True,True)

    

Step1()
Step2()
Step3()
Step4()



