#!/usr/bin/env python3
#!/usr/bin/env micropython
from ev3dev2.motor import LargeMotor,  OUTPUT_C, OUTPUT_B, follow_for_ms
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM, MoveTank, MoveSteering, SpeedPercent
from time import sleep
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
import os
import sys
os.system('setfont Lat15-TerminusBold14')

lmB = LargeMotor(OUTPUT_B)
lmC = LargeMotor(OUTPUT_C)
cs1 = ColorSensor(INPUT_1)
cs4 = ColorSensor(INPUT_4)

lmB.on(10)
lmC.on(10) 

loopCounter = 0
#while (cs4.color != ColorSensor.COLOR_BLACK and cs1.color != ColorSensor.COLOR_BLACK):
while (loopCounter < 48):
    print( "{0:02d} - CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:04d}, CS4Reflected: {3:04d}".format( 
        loopCounter, cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
    loopCounter += 1;
    sleep(.005)

lmB.off()
lmC.off()
    # print("CS1 - reflected:{0}, ambient:{1}, color:{2}", cs1.reflected_light_intensity, cs1.ambient_light_intensity, cs1.color_name, file=sys.stderr)
    # print("CS4 - reflected:{0}, ambient:{1}, color:{2}", cs4.reflected_light_intensity, cs4.ambient_light_intensity, cs4.color_name, file=sys.stderr)

    # lmB.on_for_seconds(50, .1, True, False)
    # lmC.on_for_seconds(50, .1, True, False)
    # print(cs1.reflected_light_intensity)
    # print(cs4.reflected_light_intensity)
    # print(cs1.ambient_light_intensity)
    # print(cs4.ambient_light_intensity)