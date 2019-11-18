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

cl = ColorSensor()
feeder = LargeMotor(OUTPUT_B)
penRL = LargeMotor(OUTPUT_A)
penLift = MediumMotor(OUTPUT_C)
btn = Button()

cl.mode='COL-COLOR'

print("Text: %s" % (sys.argv[1]))
colors=('unknown','black','blue','green','yellow','red','white','brown')

def penMove(x,y,penDown):
    if penDown == True and penDown != penStateDown:
        penLift.on_for_degrees(speed=defaultSpeed, degrees=-100)
    elif penDown == False and penDown != penStateDown:
        penLift.on_for_degrees(speed=defaultSpeed,degrees=100)
        

def feedIn():
    while cl.value() != 6:
        print("Color: %s", colors[cl.value()])
        feeder.on_for_degrees(speed=-50,degrees=5)
    penLift.on_for_degrees(speed=defaultSpeed, degrees=-800)



# def print_1():
    
feedIn()
sleep(20)
penMove(0,0,True)
