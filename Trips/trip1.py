#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound
import random

def runTrip1():
    sound = Sound()
    # see http://espeak.sourceforge.net/
    # values -a 200 -s 130 SHOULD BE INCLUDED if specifying any other options
    # a = amplitude (200 max, 100 default), s = speed 80-500, default = 175)
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