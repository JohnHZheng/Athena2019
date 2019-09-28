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
    TankPair.on_for_seconds(SpeedDPS(-310),SpeedDPS(-300), 2,False,True)
    TankPair.on_for_seconds(SpeedDPS(-180),SpeedDPS(-180), 1,False,True)

def Step2():   
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 200,True,True)
    TankPair.on_for_degrees(SpeedDPS(400),SpeedDPS(0), 200,True,True)
    while LeftSensor.color !=1:
        TankPair.on(SpeedDPS(150),SpeedDPS(150))
    LeftWheel.off()
    RightWheel.off()
    while LeftSensor.color != 6:
        TankPair.on(SpeedDPS(150),SpeedDPS(150))
    LeftWheel.off()
    RightWheel.off()
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 20,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(350), 145,True,True) 

    

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
        AngleNew    = 360 * LeftWheel.position / LeftWheel.count_per_rot
        DegreeSum   = DegreeSum + AngleNew - AngleOld
        AngleOld    = AngleNew
    LeftWheel.off()
    RightWheel.off()  
def Step3():  
    LineFollowing(200,70,400)
    TankPair.on_for_degrees(SpeedDPS(300), SpeedDPS(300),350,True,True )
    LineFollowing(150,40,350)
    TankPair.on_for_degrees(SpeedDPS(250), SpeedDPS(250),295,True,True )
    LeftAction.on_for_degrees(-100, 600)
    TankPair.on_for_degrees(SpeedDPS(250), SpeedDPS(300),250,True,True )
#TankPair.on_for_seconds(SpeedDPS(350), SpeedDPS(350),1,True,False )
    LeftAction.on_for_degrees(100, 600,True,True)

def Step4():
    TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(250),230,True,True )
    TankPair.on_for_degrees(SpeedDPS(-260), SpeedDPS(-260),100,True,True )
    #TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(-260),60,True,True )
    n = 0
    while n<3:
        TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(-150),30,True,True )
        TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(150),20,True,True )
        TankPair.on_for_degrees(SpeedDPS(-150), SpeedDPS(-150),40,True,True )
        n = n+1
    LeftAction.on_for_degrees(-100,700 )
    TankPair.on_for_degrees(SpeedDPS(245), SpeedDPS(245),80,True,True )
    LeftAction.on_for_degrees(100, 200)
    #TankPair.on_for_degrees(SpeedDPS(-260), SpeedDPS(0),75,True,True )
    TankPair.on_for_degrees(SpeedDPS(-245), SpeedDPS(-245),200,True,True )
    LeftAction.on_for_degrees(100,500)
     
def Step5():
    TankPair.on_for_degrees(SpeedDPS(-250), SpeedDPS(-250),415,True,True )
    TankPair.on_for_degrees(SpeedDPS(0), SpeedDPS(-250),250,True,True )
    TankPair.on_for_degrees(SpeedDPS(-250), SpeedDPS(-250),500,True,True )
    RightAction.on_for_degrees(100,1200 )
    TankPair.on_for_degrees(SpeedDPS(250), SpeedDPS(250),700,True,True )
    RightAction.on_for_degrees(100,650 )
def Step6():
    LeftAction.on_for_degrees(-50,1100)
    LeftAction.on_for_degrees(50,1100)
    RightAction.on_for_degrees(50,850)
    RightAction.on_for_degrees(-50,850)


    

Step1()
#Step2()
#Step3()
#Step4()
#Step5()
#Step6()



