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

def LineFollowing(FastSpeed,SlowSpeed,Degree):
    DegreeSum = 0
    AngleOld    = 360 * RightWheel.position / RightWheel.count_per_rot
    while DegreeSum < Degree:
        if LeftSensor.color == ColorSensor.COLOR_WHITE:
            LeftWheel.on(SpeedDPS(FastSpeed))
            RightWheel.on(SpeedDPS(SlowSpeed))
        else:
            RightWheel.on(SpeedDPS(FastSpeed))
            LeftWheel.on(SpeedDPS(SlowSpeed))  
        AngleNew    = 360 * RightWheel.position / RightWheel.count_per_rot
        DegreeSum   = DegreeSum + abs(AngleNew - AngleOld)
        AngleOld    = AngleNew
        #print(RightSensor.reflected_light_intensity,LeftSensor.reflected_light_intensity,file=sys.stderr)
    LeftWheel.off()
    RightWheel.off()
    
def Step6():
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-150), 130,True,True)
    TankPair.on_for_degrees(SpeedDPS(-300),SpeedDPS(-300), 250,True,True)
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(0))
    LineFollowing(-135,-30,100)
    LineFollowing(-75,-15,110)
    if LeftSensor.color !=1:
        TankPair.on_for_degrees(SpeedDPS(-70),SpeedDPS(0),11)                                                     
    TankPair.on_for_degrees(SpeedDPS(-300),SpeedDPS(-300), 845,True,True)
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200), 40,True,True)
    RightAction.on_for_degrees(-60, 450,True,True)
def Step7():
    while RightSensor.color != 6:
        TankPair.on(SpeedDPS(0),SpeedDPS(-50))
    while RightSensor.color != 1:
        TankPair.on(SpeedDPS(-50),SpeedDPS(-50))
    while LeftSensor.color !=1:
        TankPair.on(SpeedDPS(-50),SpeedDPS(0))
    LeftWheel.off()
    RightWheel.off    
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-100),75,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 250,True,True)
def Step8():
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200), 150,True,True)
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(0), 25,True,True)
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200), 50,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-200), 30,True,True)
    while LeftSensor.color != 6:
        TankPair.on(SpeedDPS(100),SpeedDPS(100))
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(0),SpeedDPS(-100))
    while LeftSensor.color != 6:
        TankPair.on(SpeedDPS(100),SpeedDPS(100))
    LineFollowing(-180,-80,30)
    LineFollowing(-100,-60,50) 
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-100), 9,True,True)
    TankPair.on_for_degrees(SpeedDPS(-100),SpeedDPS(-100), 50,True,True)
    while LeftSensor.color !=1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(-100))
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(-100))
    LeftWheel.off()
    RightWheel.off()
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 250,True,True)
    LineFollowing(-80,-50,150)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-100), 12,True,True)
    while LeftSensor.color !=1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(-100))
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(-100))

def Step9():
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 450,True,True)
    TankPair.on_for_seconds(SpeedDPS(0),SpeedDPS(0),10,True,False)
    LeftAction.on_for_degrees(-80,1000,True,True)
def runTrip4():     
    Step6()
    Step7()
    Step8()
    Step9()