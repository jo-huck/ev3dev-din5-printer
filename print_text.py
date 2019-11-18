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

print("Text: %s" % (sys.argv[1]))
colors=('unknown','black','blue','green','yellow','red','white','brown')

def penMove(x,y,penDown):
    global penPositionX
    global penStateDown
    if penDown == True and penDown != penStateDown:
        print("pen goes down")
        penLift.on_for_degrees(speed=defaultSpeed, degrees=-200)
        penStateDown = True
    elif penDown == False and penDown != penStateDown:
        print("pen goes up")
        penLift.on_for_degrees(speed=defaultSpeed,degrees=200)
        penStateDown = False
    if x != 0:
        print("pen moves ", x)
        penRL.on_for_degrees(speed=defaultSpeed,degrees=x)
        penPositionX += x
        print("pen position is now: ", penPositionX)
    if y != 0:
        print("pen moves ", y)
        feeder.on_for_degrees(speed=defaultSpeed, degrees=y)
        

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
    penMove(500,0,False)
    sleep(5)
    penLift.on_for_degrees(speed=defaultSpeed, degrees=800)
    feeder.on_for_degrees(speed=defaultSpeed*2, degrees=500)
    print("Paper feeding finished")


# def print_1():
feedIn()
sleep(5)
penMove(0,0,True)
sleep(5)

feedOut()
