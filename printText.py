#!/usr/bin/python3
import rawPrint

def print_text(text):
    for char in text:
        switcher={
            'A':print_A,
            'B':print_B,
            'C':print_C
        }
        func=switcher.get(char)
        func()

def getText():
    text = input("Bitte gib den zu druckenden Text ein: ")
    print_text(text)

def print_A():
    rawPrint.penMoveSlow(40,60,True)
    rawPrint.penMoveSlow(40,(-60),True)
    rawPrint.penMoveSlow(-20,25, False)
    rawPrint.penMoveSlow(-45,0,True)
    rawPrint.penMoveSlow(85,-25,False)

def print_B():
    rawPrint.penMoveSlow(80,0,True)
    rawPrint.penMoveSlow(0,40,True)
    rawPrint.penMoveSlow(-40,0,True)
    rawPrint.penMoveSlow(0,-40,True)
    rawPrint.penMoveSlow(0,40,False)
    rawPrint.penMoveSlow(-40,0,True)
    rawPrint.penMoveSlow(0,-40,True)
    rawPrint.penMoveSlow(0,50,False)#
def print_C():
    rawPrint.penMoveSlow(40,0,True)
    rawPrint.penMoveSlow(-40,0,False)
    rawPrint.penMoveSlow(0,80,True)
    rawPrint.penMoveSlow(40,0,True)
    rawPrint.penMoveSlow(10,-80,False)
def print_D:
    rawPrint.penMoveSlow(0,80,True)
    rawPrint.penMoveSlow(40,-5,True)
    rawPrint.penMoveSlow(0,-75,True)
    rawPrint.penMoveSlow(-40,-5,True)
    rawPrint.penMoveSlow(50,0,False)

rawPrint.feedIn()
getText()
rawPrint.feedOut()