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
    TankPair.on_for_seconds(SpeedDPS(-405),SpeedDPS(-400), 1.3,False,True)
    TankPair.on_for_seconds(SpeedDPS(-255),SpeedDPS(-250), 1.2,False,True)
    
def Step2():
    TankPair.on_for_degrees(SpeedDPS(250),SpeedDPS(250), 270,True,True)

def LineFollowing(Degree):
    DegreeSum = 0
    AngleOld    = 360 * LeftWheel.position / LeftWheel.count_per_rot
    while DegreeSum < Degree:
        if LeftSensor.color == ColorSensor.COLOR_WHITE:
            RightWheel.on(SpeedDPS(230))
            LeftWheel.on(SpeedDPS(80))
        else:
            LeftWheel.on(SpeedDPS(230))
            RightWheel.on(SpeedDPS(80))  
        #print("LeftSensor - color:{0}", LeftSensor.color_name, file=sys.stderr)
        AngleNew    = 360 * LeftWheel.position / LeftWheel.count_per_rot
        DegreeSum   = DegreeSum + AngleNew - AngleOld
        AngleOld    = AngleNew
    LeftWheel.off()
    RightWheel.off()    

#TankPair.on_for_seconds(SpeedDPS(-250),SpeedDPS(-150), 1)
LineFollowing(1300)
#print("LeftWheelAngleOld:{0}, LeftWheelAngleNew:{2}", AngleOld, AngleNew, file=sys.stderr)
 #def Step3():
	#TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-250),230 )

#def Step4():#TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(250), 100,True,True)
    

#sound.beep()
#print("LeftSensor - reflected:{0}, color:{1}", LeftSensor.reflected_light_intensity, LeftSensor.color_name, file=sys.stderr)
#print("RightSensor - reflected:{0}, color:{1}", RightSensor.reflected_light_intensity, RightSensor.color_name, file=sys.stderr)
Step1()
Step2()
#Step3()
