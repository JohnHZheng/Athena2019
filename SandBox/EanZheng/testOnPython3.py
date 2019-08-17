#!/usr/bin/env python3
# from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_B, OUTPUT_C
# from time import sleep
# from ev3dev2.led import Leds
from ev3dev2.sound import Sound

sound = Sound()

sound.beep()
#leds = Leds()
#leds.set_color('LEFT', 'AMBER')

""" steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C, motor_class=MediumMotor)

steer_pair.on_for_seconds(steering=0, speed=50, seconds=2) """