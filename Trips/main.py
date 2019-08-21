#!/usr/bin/env python3
from ev3dev2.button import Button
from time import sleep
from trip1 import runTrip1
btn = Button()
contin = True
while contin:
    if btn.up == True:
        runTrip1()
    elif btn.enter == True:
        contin = False
""" #!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.sound import Sound

btn = Button()
sound = Sound()

btn.wait_for_bump('left')
sound.beep()
btn.wait_for_pressed(['up', 'down'])
sound.beep()
btn.wait_for_released('right')
sound.beep() """
""" 
#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from trip1 import runTrip1
from trip2 import runTrip2
from trip3 import runTrip3
from trip4 import runTrip4

cont = True
# The master program
while cont:
    while any(brick.buttons()):
        wait(1)
    brick.display.clear()
        
    if Button.LEFT in brick.buttons():
        runTrip1()
    elif Button.UP in brick.buttons():
        runTrip2()  
    elif Button.RIGHT in brick.buttons():
        runTrip3()
    elif Button.DOWN in brick.buttons():
        runTrip4()
    elif Button.CENTER in brick.buttons():
        cont = False
    
     """