#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound
from athenaRobot import AthenaRobot
import random

def runTrip3():
    sound = Sound()
    sound.speak('This is trip three. Currently for Calibration.', espeak_opts='-a 200 -s 130 -ven+m7' + 'en+whisper', volume=100)
    robot = AthenaRobot()
    #Calibrating both sensors
    robot.OnUntilColor(85)
    #Done signal
    sound.beep()

#!/usr/bin/env pybricks-micropython
""" from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
 
def runTrip3():
    # Color Sensing
    CS = ColorSensor(Port.S4)
    if CS.color() == 1:
        brick.display.text("Black",(60,50))
    elif CS.color() == 2:
        brick.display.text("Blue",(60,50))
    elif CS.color() == 3:
        brick.display.text("Green",(60,50))
    elif CS.color() == 4:
        brick.display.text("Yellow",(60,50))
    elif CS.color() == 5:
        brick.display.text("Red",(60,50))
    elif CS.color() == 6:
        brick.display.text("White",(60,50))
    elif CS.color() == 7:
        brick.display.text("Brown",(60,50))
    else:
        brick.display.text("None", (60,50))
    wait(1000)
    brick.display.clear() """