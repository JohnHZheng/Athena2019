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
BlackThereshold = 15
WhiteThereshold = 80
#while (cs4.color != ColorSensor.COLOR_BLACK and cs1.color != ColorSensor.COLOR_BLACK):
while (loopCounter < 48):
    print( "{0:02d} - CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:03d}, CS4Reflected: {4:03d}".format( 
        loopCounter, cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
    loopCounter += 1 
    if(cs1.reflected_light_intensity > WhiteThereshold):  
        sleep(.01)
        if(cs1.reflected_light_intensity > WhiteThereshold):
            lmB.off()
            sleep(.01)
            if(cs4.reflected_light_intensity > WhiteThereshold):
                if(cs4.reflected_light_intensity > WhiteThereshold):
                    lmC.off()
                    break
    elif(cs4.reflected_light_intensity > WhiteThereshold):
        sleep(.01)
        if(cs4.reflected_light_intensity > WhiteThereshold):
            lmC.off()
            sleep(.01)
            if(cs4.reflected_light_intensity > WhiteThereshold):
                if(cs4.reflected_light_intensity > WhiteThereshold):
                    lmB.off()
                    break
lmB.on(2)
lmC.on(2)
while True:
    print( "{0:02d} - CS1: {1:10}, CS4: {2:10}, CS1Reflected: {3:03d}, CS4Reflected: {4:03d}".format( 
        loopCounter, cs1.color_name, cs4.color_name, cs1.reflected_light_intensity, cs4.reflected_light_intensity), file=sys.stderr)
    loopCounter += 1 
    if(cs1.reflected_light_intensity < BlackThereshold):
        #wsleep(.005)
        if(cs1.reflected_light_intensity < BlackThereshold):
            lmB.off()
            if(cs4.reflected_light_intensity < BlackThereshold):
                #sleep(.005)                
                lmC.off()
                break
    elif(cs4.reflected_light_intensity < BlackThereshold):
        #sleep(.005)
        if(cs4.reflected_light_intensity < BlackThereshold):
            lmC.off()        
            if(cs1.reflected_light_intensity < BlackThereshold):
                #sleep(.005)        
                lmB.off()
                break
                    

    

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