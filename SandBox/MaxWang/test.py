#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor

<<<<<<< HEAD
#LeftWheel       = LargeMotor(OUTPUT_B)
#RightWheel      = LargeMotor(OUTPUT_C)

TankPair        = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
LeftSensor      = ColorSensor(INPUT_1)
RightSensor     = ColorSensor(INPUT_4)
N = 0
#while N<4:
    #TankPair.on_for_seconds(SpeedDPS(-400),SpeedDPS(-400), 1)
    #TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(250),115,True,True)
    # N = N + 1
=======
>>>>>>> 8c5914dbd59ea2113de00c06e2cc0afc2281b666

    
    
    


