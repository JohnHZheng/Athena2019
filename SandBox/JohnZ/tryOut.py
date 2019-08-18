#!/usr/bin/env python3
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
