#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor

lmB = LargeMotor(OUTPUT_B)
lmC = LargeMotor(OUTPUT_C)

# lmB.on_for_seconds(90, 1, True, False)
# lmC.on_for_seconds(90, 1)

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
steer_pair.on_for_seconds(0, 50, 3)

#tank_pair.on_for_seconds(50,50,1)
#tank_pair.on_for_seconds(-50,-50,1)
""" tank_pair.cs = ColorSensor()
tank_pair.follow_line(
    kp=11.3, ki=0.05, kd=3.2,
    speed=SpeedPercent(5),
    follow_for=follow_for_ms,
    ms=4500
    ) """
# turn on both motors at the same time block = false
# lmB.on_for_seconds(50,2, True, False)
# lmC.on_for_seconds(50,2, True, True)

#lmB.on_for_seconds(speed = 50, seconds=1)

# lmB.on_for_seconds( seconds=1, speed = 50)

# lmB.on_for_seconds(90, 1)
#lmB.on(speed=50)
#lmB.wait_until_not_moving()
'''
This will run the large motor at 50% of its
rated maximum speed of 1050 deg/s.
50% x 1050 = 525 deg/s
'''
""" lmB.on_for_seconds(speed = 50, seconds=1)
sleep(1)
lmC.on_for_seconds(speed = 50, seconds=1)

sleep(1)
lmB.on_for_seconds(90, 1)
lmC.on_for_seconds(90, 1) """

'''
This will run at 500 degrees per second (DPS).
You should be able to hear that the motor runs a
little slower than before.
'''
""" lmB.on_for_seconds(speed=SpeedDPS(500), seconds=1)
sleep(1)

# 36000 degrees per minute (DPM) (rarely useful!)
lmB.on_for_seconds(speed=SpeedDPM(36000), seconds=1)
sleep(1)

# 2 rotations per second (RPS)
lmB.on_for_seconds(speed=SpeedRPS(2), seconds=1)
sleep(1)

# 100 rotations per minute(RPM)
lmB.on_for_seconds(speed=SpeedRPM(100), seconds=1) """


''' runnable line follow
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_drive.cs = ColorSensor()

#tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), .5)
tank_drive.follow_line(
    kp=11.3, ki=0.05, kd=3.2,
    speed=SpeedPercent(10),
    follow_for=follow_for_ms,
    ms=4500
    )
    '''
