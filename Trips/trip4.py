#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound
import random

def runTrip4():
    sound = Sound()
    sound.speak('This is trip four. More to come...', espeak_opts='-a 200 -s 130 -ven+m7', volume=100)
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