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
    left = LargeMotor(OUTPUT_B)
    right = LargeMotor(OUTPUT_C)
    x=0
    thingsToTalk = ["Go Athena", "Yeah, we won, we rocks", "We are the Champions","Lets Go Athena Lets Go","Oops"]
    toneOptions=['en+m7', 'en+f1', 'en+f5','en+m1','en+croak','en+whisper', 'en-rp']
    talkRandom = random.SystemRandom()
    toneRandom = random.SystemRandom()
    for x in range(5):
        leds.set_color('LEFT', 'RED')
        sleep(0.1)
        leds.set_color('RIGHT', 'RED')
        sleep(0.1)
        """ brick.display.text("Go Athena!!!",(50,60))
        leftWheel.run_target(3000,360,Stop.BRAKE) """
        leds.set_color('LEFT', 'YELLOW')
        sleep(0.1)
        leds.set_color('RIGHT', 'YELLOW')
        sleep(0.1)

        opts = '-a 200 -s 130 -v'
        sound.speak(talkRandom.choice(thingsToTalk), espeak_opts=opts + toneRandom.choice(toneOptions), volume=100) # long form
        
        leds.set_color('LEFT', 'ORANGE')
        sleep(0.1)
        leds.set_color('RIGHT', 'ORANGE')
        
