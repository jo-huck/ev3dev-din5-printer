#!/usr/bin/python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')

penLift = MediumMotor(OUTPUT_C)
penMove = LargeMotor(OUTPUT_A)
btn = Button()

penLift.on_for_degrees(speed=40, degrees=-850)
penMove.on_for_degrees(speed=20, degrees=500)
sleep(2)
while True:
    penMove.on_for_degrees(speed=20, degrees=-1000)
    penLift.on_for_degrees(speed=-20, degrees=10)
    if btn.enter:
        penMove.on_for_degrees(speed=20, degrees=500)
        penLift.on_for_degrees(speed=20, degrees=900)
        break
    penMove.on_for_degrees(speed=20, degrees=1000)
    penLift.on_for_degrees(speed=-20, degrees=10)
    if btn.enter:
        penMove.on_for_degrees(speed=20, degrees=-500)
        penLift.on_for_degrees(speed=20, degrees=900)
        break
