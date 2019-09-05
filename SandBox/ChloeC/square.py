#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from time import sleep
from athenaRobot import AthenaRobot

thing = AthenaRobot()
thing.run(10, 15)
sleep(0.1)
thing.turn(-90)
thing.run(10, 15)
sleep(0.1)
thing.turn(-90)
thing.run(10, 15)
sleep(0.1)
thing.turn(-90)
thing.run(10, 15)