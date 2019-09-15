#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound
from athenaRobot import AthenaRobot
import random

def runTrip4():
    #tank = MoveTank(OUTPUT_B, OUTPUT_C)
    #tank.on_for_rotations(left_speed=30, right_speed=30, rotations=3)
    #sound = Sound()
    #sound.speak('This is trip four. More to come...', espeak_opts='-a 200 -s 130 -ven+m7', volume=100)
    robot = AthenaRobot()
    robot.turn(35)
    robot.run(60, 20)
    robot.onUntilWhiteLine()
    #sleep.0.1
    robot.turn(-90)

    # Those are old code 
    # robot.turn(22)
    # robot.run(40, 20)
    # robot.turn(-32)
    # robot.onUntilGameLine()
    # robot.turn(-110)
    # robot.onUntilLeftWhite()

    # robot.turn(90)
    # sleep(.3)
    # robot.turn(90)
    # sleep(.3)
    # robot.turn(-90)
    # sleep(.3)
    # robot.turn(-90)
    # sleep(.3)   
    # robot.onUntilGameLine()
    # robot.turn(-90)
    # robot.onUntilLeftWhite()
    #robot.onUntilGameLine()
    # robot.goToBridge()
    """ for x in range(4):
        #robot.run(10,10)
        robot.turn(90,15)
        robot.run(20,20) """
        
    #robot.onUntilBlackLine()
    """ robot.run(10,10)
    robot.turn(90)
    robot.turn(-90)
    robot.onUntilGameLine()
 """
""" #!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from helpers import advLineFollow
 
def runTrip4():
    #lineFollow
    #lineFollow()
    advLineFollow(150, 25, 90)
    # Circle
    leftWheel = Motor(Port.B)
    rightWheel = Motor(Port.C)
    robot = DriveBase(leftWheel,rightWheel,100,156)
    robot.drive_time(100,100,5000) """