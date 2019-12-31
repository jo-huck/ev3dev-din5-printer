#!/usr/bin/python3
import rawPrint

def print_text(text):
    for char in text:
        switcher={
            'A':print_A,
            'B':print_B,
            'C':print_C,
            'D':print_D,
            ' ':print_space
        }
        func=switcher.get(char)
        func()

def getText():
    text = input("Bitte gib den zu druckenden Text ein: ")
    print_text(text)

def print_A():
    rawPrint.penMoveSlow(40,60,True) # Linker Schrägstrich
    rawPrint.penMoveSlow(40,(-60),True) # Rechter Schrägstrich
    rawPrint.penMoveSlow(-20,25, False) # zum startpunkt des Strichs bewegen
    rawPrint.penMoveSlow(-45,0,True) # Strich zeichnen
    rawPrint.penMoveSlow(85,-25,False) # zur Endposition fahren

def print_B():
    rawPrint.penMoveSlow(0,60,True)
    rawPrint.penMoveSlow(30,0,True)
    rawPrint.penMoveSlow(20,-18,True)
    #rawPrint.penMoveSlow(0,-10,True)
    rawPrint.penMoveSlow(-20,-18,True)
    rawPrint.penMoveSlow(-30,0,True)
    rawPrint.penMove(30,0,False)
    rawPrint.penMoveSlow(20,-12,True)
    #rawPrint.penMoveSlow(0,-10,True)
    rawPrint.penMoveSlow(-20,-12,True)
    rawPrint.penMoveSlow(-30,0,True)
    rawPrint.penMove(60,0,False)
def print_C():
    print("Not implemented: C")
def print_D():
    print("Not implemented: D")
def print_space():
    rawPrint.penMove(50,0,False)

rawPrint.feedIn()
getText()
rawPrint.feedOut()