#!/usr/bin/python3
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from time import sleep

defaultSpeed = 20

penStateDown = False
penPositionX = 500

cl = ColorSensor()
feeder = LargeMotor(OUTPUT_B)
penRL = LargeMotor(OUTPUT_A)
penLift = MediumMotor(OUTPUT_C)
btn = Button()

cl.mode='COL-COLOR'

# print("Text: %s" % (sys.argv[1]))
colors=('unknown','black','blue','green','yellow','red','white','brown')

def penMove(x,y,penDown):
    global penPositionX
    global penStateDown
    xSpeed = defaultSpeed
    ySpeed = defaultSpeed
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
            xSpeed = defaultSpeed * (x/y)
            print("--> Calculated xSpeed: ", xSpeed)
        print("pen moves ", x)
        penRL.on_for_degrees(speed=xSpeed,degrees=x,block=(y == 0))
        penPositionX += x
        print("pen position is now: ", penPositionX)
    if y != 0:
        if (x>y and y != 0 and x/y != 0):
            ySpeed = defaultSpeed * (y/x)
            print("--> Calculated ySpeed: %s", ySpeed)
        print("pen moves ", -(y/2))
        feeder.on_for_degrees(speed=ySpeed, degrees=-y)



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

# x = R/L
# y = F/B
# def print_1():
feedIn()
sleep(2)
penMove(x=500,y=500,penDown=True)
sleep(2)

feedOut()
