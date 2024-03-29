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
        #print(RightSensor.reflected_light_intensity,LeftSensor.reflected_light_intensity,file=sys.stderr)
    LeftWheel.off()
    RightWheel.off()


def Step1():
    TankPair.on_for_seconds(SpeedDPS(-360),SpeedDPS(-300), 2,False,True)
    TankPair.on_for_seconds(SpeedDPS(-150),SpeedDPS(-150), 1.1,False,True)
    RightAction.on_for_degrees(50,350)
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200),70 ,False,True)
    RightAction.on_for_degrees(-50,350)
    

def Step2():
    TankPair.on_for_degrees(SpeedDPS(300),SpeedDPS(300), 150,True,True)
    TankPair.on_for_degrees(SpeedDPS(400),SpeedDPS(0), 200,True,True)
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-250),SpeedDPS(-250))
    while RightSensor.color != 6:
        TankPair.on(SpeedDPS(-250),SpeedDPS(-250))
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 90,True,True)
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    LeftWheel.off()
    RightWheel.off()
    LineFollowing(-180,-50,150)
    #LineFollowing(-100,-0,120)
    if RightSensor.color == 1:
        TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-100), 10,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),250,True,True)
    while LeftSensor.color !=6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    while LeftSensor.color !=1:
        TankPair.on(SpeedDPS(-200),SpeedDPS(-200))
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),75,True,True)
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(-250),SpeedDPS(-0))
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(-250),SpeedDPS(-0))
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),50,True,True)
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(0),SpeedDPS(-250))
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(0),SpeedDPS(-250))
    LineFollowing(-100,-0,100)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-100),10,True,True)
    if RightSensor.color == 1:
        TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-100),20,True,True)
    RightAction.on_for_degrees(50,600,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 155,True,True)
    RightAction.on_for_degrees(-50,600)

def Step3():  
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-150), 245,True,True)
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(-200), 200,True,True)
    TankPair.on_for_degrees(SpeedDPS(200), SpeedDPS(0),115,True,True )
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200), 130,True,True)
    TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(200),120,True,True )
    RightAction.on_for_degrees(80,400,True,True)
    TankPair.on_for_degrees(SpeedDPS(300),SpeedDPS(300), 180,True,True)
    RightAction.on_for_degrees(-80,400,False,True)

def Step4():
    LeftAction.on_for_degrees(-50,1400,True,False)
    #TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),10,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-250),170,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),290,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(0),430,True,True)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),30,True,True)
    LeftAction.on_for_degrees(100,200,True,True)
    LeftAction.on_for_degrees(100,1200,False,True)



def Step5():
    TankPair.on_for_degrees(SpeedDPS(600),SpeedDPS(595),2700,False,True)


def runTrip3():
    Step1()
    Step2()
    Step3()
    Step4()
    Step5()