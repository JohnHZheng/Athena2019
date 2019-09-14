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
LeftAction      = MediumMotor(OUTPUT_A)
RightAction     = MediumMotor(OUTPUT_D)
TankPair        = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
LeftSensor      = ColorSensor(INPUT_1)
RightSensor     = ColorSensor(INPUT_4)
LeftWheel       = LargeMotor(OUTPUT_B)
RightWheel      = LargeMotor(OUTPUT_C)

def Step1():
    TankPair.on_for_seconds(SpeedDPS(-405),SpeedDPS(-400), 1.3,False,True)
    TankPair.on_for_seconds(SpeedDPS(-255),SpeedDPS(-250), 1.2,False,True)
    
def Step2():
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 270,True,True)



#print("LeftSensor - reflected:{0}, ambient:{1}, color:{2}", LeftSensor.reflected_light_intensity, LeftSensor.ambient_light_intensity, LeftSensor.color_name) #, file=sys.stderr)
 
Step1()
#Step2()
#Step3()
