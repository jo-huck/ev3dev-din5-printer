#!/usr/bin/python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
#from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
# from ev3dev2.led import Leds
from ev3dev2.button import Button
from time import sleep

defaultSpeed = 20
slowSpeed = 15
penStateDown = False
penPositionX = 500

cl = ColorSensor()
feeder = LargeMotor(OUTPUT_B)
penRL = LargeMotor(OUTPUT_A)
penLift = MediumMotor(OUTPUT_C)
btn = Button()

cl.mode='COL-COLOR'

colors=('unknown','black','blue','green','yellow','red','white','brown')

def toPositive(x,y=0):
    if x<0:
        print("inverted value: ", x*(-1))
        return x*(-1)
    else:
        print("unchanged value: ", x)
        return x
def both_negative(x,y):
    if x<0: #and y<0:
        return x*-1
    else:
        return x

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
    
        if (both_negative(y,x)>both_negative(x,y) and x != 0 and y/x != 0):
            # xSpeed = (defaultSpeed / (y/x)) * 2
            xSpeed = speed * (toPositive(x,y)/toPositive(y,x))
            print("--> Calculated xSpeed: ", xSpeed)
        print("pen moves ", x)
        penRL.on_for_degrees(speed=xSpeed,degrees=x,block=(y == 0),brake=True)
        penPositionX += x
        print("pen position is now: ", penPositionX)
    if y != 0:
        if (both_negative(x,y)>both_negative(y,x) and y != 0 and x/y != 0):
            ySpeed = speed * (toPositive(y,x)/toPositive(x,y))
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
