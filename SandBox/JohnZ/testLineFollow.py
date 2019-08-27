#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

lmB = LargeMotor(OUTPUT_B)
lmC = LargeMotor(OUTPUT_C)

# lmB.on_for_seconds(90, 1, True, False)
# lmC.on_for_seconds(90, 1)

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)


#tank_pair.on_for_seconds(50,50,1)
#tank_pair.on_for_seconds(-50,-50,1)
tank_pair.cs = ColorSensor(INPUT_1)
tank_pair.follow_line(
    kp=11.3, ki=0.05, kd=3.2,
    speed=SpeedPercent(5),
    follow_for=follow_for_ms,
    ms=9000
    )