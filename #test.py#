#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.button import Button
from time import sleep
from ev3dev2.sound import Sound
import os
os.system('setfont Lat15-TerminusBold14')

penHeight = 0
penPosition = 0
feeder = LargeMotor(OUTPUT_B)
penMove = LargeMotor(OUTPUT_A)
penLift = MediumMotor(OUTPUT_C)
btn = Button()


def screenClear():
    for i in range(10):
        print()


# sound = Sound()
# sound.play_file('/home/robot/music/cold.wav', volume=50, play_type=2)
while True:
    if btn.up:
        penLift.on_for_degrees(speed=20, degrees=2)
        penHeight += 2
    if btn.down:
        penLift.on_for_degrees(speed=20, degrees=-2)
        penHeight -= 2
    if btn.left:
        penMove.on_for_degrees(speed=20, degrees=2)
        penPosition += 2
    if btn.right:
        penMove.on_for_degrees(speed=20, degrees=-2)
        penPosition -= 2
    if btn.enter:
        screenClear()
        print('L/R: ' + str(penPosition))
        print('Height: ' + str(penHeight))
        sleep(10)
        penMove.on_for_degrees(speed=30,
                               degrees=(penPosition - penPosition) -
                               penPosition)
        sleep(2)
        penLift.on_for_degrees(speed=30,
                               degrees=(penHeight - penHeight) - penHeight)
        break

# feeder.on_for_rotations(SpeedPercent(-30), 10)
# penLift.on_for_rotations(speed=20, rotations=-1)
# penMove.on_for_rotations(speed=20, rotations=1)
