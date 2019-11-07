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
def linefollowing2(FastSpeed,SlowSpeed,Degree):
    DegreeSum = 0
    AngleOld    = 360 * RightWheel.position / RightWheel.count_per_rot
    while DegreeSum < Degree:
        if RightSensor.color == ColorSensor.COLOR_WHITE:
            RightWheel.on(SpeedDPS(FastSpeed))
            LeftWheel.on(SpeedDPS(SlowSpeed))
        else:
            LeftWheel.on(SpeedDPS(FastSpeed))
            RightWheel.on(SpeedDPS(SlowSpeed))  
        AngleNew    = 360 * RightWheel.position / RightWheel.count_per_rot
        DegreeSum   = DegreeSum + abs(AngleNew - AngleOld)
        AngleOld    = AngleNew
        #print(RightSensor.reflected_light_intensity,LeftSensor.reflected_light_intensity,file=sys.stderr)
    LeftWheel.off()
    RightWheel.off()

def Step7():
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250), 1400,True,True)
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 60,True,True)
    LeftAction.on_for_degrees(SpeedDPS(-500),900,True,True)
   
def Step8():
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),250,True,True)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-200),220,True,True)
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(-200),50,True,True)
    TankPair.on_for_degrees(SpeedDPS(200),SpeedDPS(200),180,True,True)
def Step9():
    while LeftSensor.color !=6:
        TankPair.on(SpeedDPS(0),SpeedDPS(-200))
    while LeftSensor.color !=1:
        TankPair.on(SpeedDPS(0),SpeedDPS(-200))
    while LeftSensor.color !=6:
        TankPair.on(SpeedDPS(0),SpeedDPS(-200))   
    TankPair.on_for_degrees(SpeedDPS(-200),SpeedDPS(-200),75,True,True)
    while LeftSensor.color !=6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    while RightSensor.color !=6:
        TankPair.on(SpeedDPS(-200),SpeedDPS(0))
    RightWheel.off()
    LeftWheel.off()
    TankPair.on_for_degrees(SpeedDPS(-500),SpeedDPS(-500),600,True,True)
    TankPair.on_for_seconds(SpeedDPS(0),SpeedDPS(0),10,True,True)


def runTrip3():  
    Step7()
    Step8()
    Step9()

