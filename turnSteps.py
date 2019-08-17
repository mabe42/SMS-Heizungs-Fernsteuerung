#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from http://www.elektronx.de/tutorials/schrittmotorsteuerung-mit-dem-raspberry-pi/

# import required modules
import sys
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Verwendete Pins am Rapberry Pi
A=7
B=8
C=9
D=11
time = 0.005

# Pins aus Ausgänge definieren
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)

# Schritte 1 - 8 festlegen
def Step1():
    GPIO.output(D, True)
    sleep (time)
    GPIO.output(D, False)

def Step2():
    GPIO.output(D, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(C, False)

def Step3():
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(C, False)

def Step4():
    GPIO.output(B, True)
    GPIO.output(C, True)
    sleep (time)
    GPIO.output(B, False)
    GPIO.output(C, False)

def Step5():
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(B, False)

def Step6():
    GPIO.output(A, True)
    GPIO.output(B, True)
    sleep (time)
    GPIO.output(A, False)
    GPIO.output(B, False)

def Step7():
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(A, False)

def Step8():
    GPIO.output(D, True)
    GPIO.output(A, True)
    sleep (time)
    GPIO.output(D, False)
    GPIO.output(A, False)
   
def main(steps):
  steps = int(steps)
  if (steps < 0):
    steps *= -1
    # cw - abdrehen
#    print "Jetzt wirds kalt\n"
    for i in range (steps):    
      Step1()
      Step2()
      Step3()
      Step4()
      Step5()
      Step6()
      Step7()
      Step8()  

  else:
    # ccw - aufdrehen
#    print "Jetzt wirds warm\n"
    for i in range (steps):
      Step8()
      Step7()
      Step6()
      Step5()
      Step4()
      Step3()
      Step2()
      Step1()
      
if __name__ == "__main__":
   main(sys.argv[1])
