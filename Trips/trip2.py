#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep
def PanelDemo():
        tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
        UnD = MediumMotor(OUTPUT_D)
        LnR = MediumMotor(OUTPUT_A)
        tank_pair.on_for_rotations(right_speed=20, left_speed=40, rotations=2)
        tank_pair.on_for_rotations(left_speed=20, right_speed=40, rotations=2)
        UnD.on_for_seconds(speed = 10, seconds = 3)
        LnR.on_for_seconds(speed = -10, seconds = 3)
        UnD.on_for_seconds(speed = -70, seconds = .5)
        LnR.on_for_seconds(speed = 70, seconds = .5)
        #going forward while moving both motors
        UnD.on_for_seconds(speed = 70, seconds = .5, block = False)
        LnR.on_for_seconds(speed = -70, seconds = .5, block = False)
        tank_pair.on_for_seconds(right_speed=30,left_speed=30,seconds=.5)
        #going backwards while restoring both motors
        UnD.on_for_seconds(speed = -10, seconds = 3, block = False)
        LnR.on_for_seconds(speed = 10, seconds = 3, block = False)
        tank_pair.on_for_seconds(right_speed=-10,left_speed=-10,seconds=3)