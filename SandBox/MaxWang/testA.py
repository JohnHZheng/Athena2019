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

def LineFollowing(FastSpeed,SlowSpeed,Degree):
    DegreeSum = 0
    AngleOld    = 360 * RightWheel.position / RightWheel.count_per_rot
    while DegreeSum < Degree:
        if RightSensor.color == ColorSensor.COLOR_WHITE:
            LeftWheel.on(SpeedDPS(FastSpeed))
            RightWheel.on(SpeedDPS(SlowSpeed))
        else:
            RightWheel.on(SpeedDPS(FastSpeed))
            LeftWheel.on(SpeedDPS(SlowSpeed))  
        AngleNew    = 360 * RightWheel.position / RightWheel.count_per_rot
        DegreeSum   = DegreeSum + abs(AngleNew - AngleOld)
        AngleOld    = AngleNew
    LeftWheel.off()
    RightWheel.off()


def Step1():
    TankPair.on_for_seconds(SpeedDPS(-310),SpeedDPS(-300), 2,False,True)
    TankPair.on_for_seconds(SpeedDPS(-180),SpeedDPS(-180), 1,False,True)

def Step2():   
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 150,True,True)
    TankPair.on_for_degrees(SpeedDPS(400),SpeedDPS(0), 150,True,True)
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    while RightSensor.color != 6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    LeftWheel.off()
    RightWheel.off()
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 90,True,True)
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    LeftWheel.off()
    RightWheel.off()
    LineFollowing(-180,-50,230)
    LineFollowing(-100,-0,120)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),200,True,True)
    while LeftSensor.color !=6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    LeftWheel.off()
    RightWheel.off()
    LineFollowing(-100,-0,100)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 130,True,True)
    LineFollowing(-100,-0,100)
    RightAction.on_for_degrees(50,850,True,True)
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(0),SpeedDPS(-100))
    LeftWheel.off()
    RightWheel.off()
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 130,True,True)
    RightAction.on_for_degrees(-50,850)

def Step3():  
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-250), 240,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 240,True,True)
    TankPair.on_for_degrees(SpeedDPS(250), SpeedDPS(0),90,True,True )
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 160,True,True)
    TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(250),110,True,True )
    RightAction.on_for_degrees(50,850,True,True)
    TankPair.on_for_degrees(SpeedDPS(150),SpeedDPS(300), 130,True,True)
    RightAction.on_for_degrees(-50,425,True,True)
    TankPair.on_for_degrees(SpeedDPS(150),SpeedDPS(300), 150,True,True)
    RightAction.on_for_degrees(-50,425,True,True)

def Step4():
    TankPair.on_for_degrees(SpeedDPS(150),SpeedDPS(0), 125,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-250), 160,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),650,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(300), 175,True,True)
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(0),SpeedDPS(150))
    while RightSensor.color !=1: 
        TankPair.on(SpeedDPS(0),SpeedDPS(150))
    LeftWheel.off()
    RightWheel.off()
    LineFollowing(-150,-30,300)
    LeftAction.on_for_degrees(-50,1200,True,True) 
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),150,True,True)
    LeftAction.on_for_degrees(50,1200,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(250),100,True,True)
    
Step1()
Step2()
#Step3()
#Step4()






