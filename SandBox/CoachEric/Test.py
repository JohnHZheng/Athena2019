


    TankPair        = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(-250),143,True,True)
n = 0
while n<4:
    TankPair        = MoveTank(OUTPUT_C, OUTPUT_B, motor_class=LargeMotor)
    TankPair.on_for_degrees(SpeedDPS(-250),SpeedDPS(250),115,True,True)
    n = n+1
 TankPair        = MoveTank(OUTPUT_B, OUTPUT_C, motor_class=LargeMotor)
    TankPair.on_for_degrees(SpeedDPS(0),SpeedDPS(-250),230 
RightAction.on_for_seconds(-100, 0.5)

LeftAction.on_for_seconds(100, 0.6)
sleep(2)
LeftAction.on_for_seconds(100, 0.6)
sleep(2)
LeftAction.on_for_seconds(-100, 1.2)




