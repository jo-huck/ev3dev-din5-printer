#!/usr/bin/python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
#from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# from ev3dev2.led import Leds
from ev3dev2.button import Button
from time import sleep

defaultSpeed = 20
slowSpeed = 10
penStateDown = False
penPositionX = 500

cl = ColorSensor()
feeder = LargeMotor(OUTPUT_B)
penRL = LargeMotor(OUTPUT_A)
penLift = MediumMotor(OUTPUT_C)
btn = Button()

cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')

def toPositive(value):
    if (value<0):
        return value*(-1)
    else:
        return value

def penMoveSpeed(x,y,penDown,speed):
    global penPositionX
    global penStateDown
    xSpeed = speed
    ySpeed = speed
    if penDown == True and penDown != penStateDown:
        print("pen goes down")
        penLift.on_for_degrees(speed=defaultSpeed, degrees=-200)
        penStateDown = True
    elif penDown == False and penDown != penStateDown:
        print("pen goes up")
        penLift.on_for_degrees(speed=defaultSpeed,degrees=200)
        penStateDown = False

    if x != 0:
    
        if (y>x and x != 0 and y/x != 0):
            # xSpeed = (defaultSpeed / (y/x)) * 2
            xSpeed = speed * (toPositive(x)/toPositive(y))
            print("--> Calculated xSpeed: ", xSpeed)
        print("pen moves ", x)
        penRL.on_for_degrees(speed=xSpeed,degrees=x,block=(y == 0),brake=True)
        penPositionX += x
        print("pen position is now: ", penPositionX)
    if y != 0:
        if (x>y and y != 0 and x/y != 0):
            ySpeed = speed * (toPositive(y)/toPositive(x))
            print("--> Calculated ySpeed: %s", ySpeed)
        print("pen moves ", -(y))
        feeder.on_for_degrees(speed=ySpeed, degrees=y,brake=True)
def penMove(x,y,penDown):
    penMoveSpeed(x,y,penDown,defaultSpeed)
def penMoveSlow(x,y,penDown):
    penMoveSpeed(x,y,penDown,slowSpeed)
def feedIn():
    print("feeding paper in")
    while cl.value() != 6:
        print("Color: %s", colors[cl.value()])
        feeder.on_for_degrees(speed=defaultSpeed,degrees=-20)
    penLift.on_for_degrees(speed=defaultSpeed, degrees=-700)
    penMove(-500,0,False)
    print("Paper feeding finished")

def feedOut():
    print("feeding paper out")
    penMove(500-penPositionX,0,False)
    sleep(0.5)
    penLift.on_for_degrees(speed=defaultSpeed, degrees=700)
    feeder.on_for_degrees(speed=defaultSpeed*2, degrees=500)
    print("Paper feeding finished")
