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
    
def Step1():
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-150), 150,True,True)
    TankPair.on_for_degrees(SpeedDPS(-300),SpeedDPS(-300), 250,True,True)
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(0))
    LineFollowing(-180,-50,100)
    LineFollowing(-100,-20,110)
    if LeftSensor.color !=1:
        TankPair.on_for_degrees(SpeedDPS(-70),SpeedDPS(0),9)   
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(-200), 870,True,True)
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200), 65,True,True)
    RightAction.on_for_degrees(-60,800,True,True)
def Step2():
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(-100),SpeedDPS(-100))
    while LeftSensor.color != 6:
        TankPair.on(SpeedDPS(-100),SpeedDPS(-100))   
    """
    while RightSensor.color != 1:
        TankPair.on(SpeedDPS(0),SpeedDPS(-100))
    while LeftSensor.color != 1:
        TankPair.on(SpeedDPS(-75),SpeedDPS(-75)) 
    while RightSensor.color !=1:
        TankPair.on(SpeedDPS(0),SpeedDPS(-75))
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(0),SpeedDPS(-75)) 
    """
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-200), 165,True,True)
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(-200), 230,True,True)


Step1()
Step2()
#Step3()
#Step4()
