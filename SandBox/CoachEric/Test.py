#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor

lmB = LargeMotor(OUTPUT_B)
lmC = LargeMotor(OUTPUT_C)

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on_for_seconds(0, 50, 3)
