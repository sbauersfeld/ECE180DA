#!/usr/bin/python3.7

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Delay in seconds
wait = 5

LED = [int(i) for i in input("Enter GPIO pins: ").split()]

#Turn on LEDs
for i in LED:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

time.sleep(wait)

#Turn off LEDs
for i in LED:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)
