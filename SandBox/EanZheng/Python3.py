#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
motor = LargeMotor(OUTPUT_C)
tank_pair = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
steer_pair = MoveSteering(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
csl = ColorSensor(INPUT_4)
csr = ColorSensor(INPUT_1)

while csl.color != 1 and csr.color != 1:
    tank_pair.on(70,70)

"""motor.on(speed=30)
motor.wait_until_not_moving()
tank_pair.on_for_degrees(-100,100,720, brake=True, block=True)
tank_pair.on_for_degrees(60,60,90, brake=True, block=True)
steer_pair.on_for_degrees(60,60,90, brake=True, block=True) """
