#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_C, OUTPUT_B, OUTPUT_D, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import math
import sys 
from athenaRobot import AthenaRobot

# wheel constances in Center Meter
wheelRadiusCm = 2.75 
wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
leftMotor = LargeMotor(OUTPUT_C)
rightMotor = LargeMotor(OUTPUT_B) 
leftSensor = ColorSensor(INPUT_4)
rightSensor = ColorSensor(INPUT_1)
forkliftMtr= MediumMotor(OUTPUT_D)

def runTrip1():
    sound = Sound()
    leds = Leds()
	# Four lists to randomize the quotes, voices, colors, and lights.
    thingsToTalk = ["Go Athena", "Yeah, we won, we rock", "We are the Champions","Lets Go Athena Lets Go","we are big brain"]
    toneOptions=['en+m7', 'en+f1', 'en+f5','en+m1','en+croak','en+whisper', 'en-rp']
    ColorOptions = ['BLACK','RED','ORANGE','AMBER','YELLOW','GREEN']
    SideOptions = ['LEFT','RIGHT']
	# Four randoms to randomize the quotes, voices, colors, and lights as well.
    talkRandom = random.SystemRandom()
    toneRandom = random.SystemRandom()
    ColorRandom = random.SystemRandom()
    SideRandom = random.SystemRandom()
	# Options for speak
    opts = '-a 200 -s 130 -v'
    for x in range(5):
        for y in range(3):
			# Randomizing the Colors and Sides for the light 3 times
            leds.set_color(SideRandom.choice(SideOptions), ColorRandom.choice(ColorOptions))
            sleep(0.1)
            leds.set_color(SideRandom.choice(SideOptions), ColorRandom.choice(ColorOptions))
            sleep(0.1)
        # Randomizing the volume, tone, and quote.
        sound.speak(talkRandom.choice(thingsToTalk), espeak_opts=opts + toneRandom.choice(toneOptions), volume=100) # long form
def Trip1Tryout(): 
    wheelRadiusCm = 4
    wheelCircumferenceCm = 2 * math.pi * wheelRadiusCm
    leftMotor = LargeMotor(OUTPUT_C)
    rightMotor = LargeMotor(OUTPUT_B) 
    leftSensor = ColorSensor(INPUT_4)
    rightSensor = ColorSensor(INPUT_1)
    forkliftMtr= MediumMotor(OUTPUT_D)
    robot = AthenaRobot()
    robot.turn(90)
    robot.run(-7,14)
    """ robot.run(70,30,brake=True)
    robot.onUntilGameLine()
    robot.turn(360) """
#Trip1Tryout()
