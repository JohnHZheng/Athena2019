#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor

lmB = LargeMotor(OUTPUT_B)
lmC = LargeMotor(OUTPUT_C)

lmB.on_for_seconds(90, 1, True, False)
lmC.on_for_seconds(90, 1)
