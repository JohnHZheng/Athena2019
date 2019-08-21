#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
def runTrip1():
    leds = Leds()
    left = LargeMotor(OUTPUT_B)
    right = LargeMotor(OUTPUT_C)
    x=0
    for x in range(5):
        leds.set_color('LEFT', 'RED')
        leds.set_color('RIGHT', 'RED')
        """ brick.display.text("Go Athena!!!",(50,60))
        leftWheel.run_target(3000,360,Stop.BRAKE) """
        leds.set_color('LEFT', 'YELLOW')
        leds.set_color('RIGHT', 'YELLOW')
        #leftWheel.run_target(3000,-360,Stop.BRAKE)
        leds.set_color('LEFT', 'ORANGE')
        leds.set_color('RIGHT', 'ORANGE')
        
    #brick.sound.file(SoundFile.CHEERING)
""" def ColSnsR():
    csl = ColorSensor(INPUT_4)
    csr = ColorSensor(INPUT_1)
    tank_pair = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
    while csl.color != 1 and csr.color != 1:
        tank_pair.on(70,70)
    tank_pair.off()
ColSnsR()
 """
""" #!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

def runTrip1():
    # Dance routine
    leftWheel = Motor(Port.B)
    rightWheel = Motor(Port.C)
    x=0
    for x in range(5):
            brick.light(Color.RED)
            brick.display.text("Go Athena!!!",(50,60))
            leftWheel.run_target(3000,360,Stop.BRAKE)
            brick.light(Color.YELLOW)
            leftWheel.run_target(3000,-360,Stop.BRAKE)
            brick.light(Color.ORANGE)
    brick.sound.file(SoundFile.CHEERING)
 """
