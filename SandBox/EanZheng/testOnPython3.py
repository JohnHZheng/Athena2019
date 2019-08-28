#!/usr/bin/env micropython
#from ev3dev.ev3 import *
#import os
# os.system('setfont Lat15-TerminusBold14')
# mL = LargeMotor('outB'); mL.stop_action = 'hold'
# mR = LargeMotor('outC'); mR.stop_action = 'hold'
# print('Hello, my name is EV3!')
# Sound.speak('Hello, my name is Ean Zheng. And I am 13 years old!').wait()
# mL.run_to_rel_pos(position_sp= 840, speed_sp = 250)
# mR.run_to_rel_pos(position_sp=-840, speed_sp = 250)
# mL.wait_while('running')
# mR.wait_while('running')
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_drive.on_for_rotations(left_speed=50, right_speed=75, rotations=10)
""" tank_drive.follow_line( kp=11.3, ki=0.05, kd=3.2,
        speed=SpeedPercent(30),
        follow_for=follow_for_ms,
        ms=4500
    ) """
