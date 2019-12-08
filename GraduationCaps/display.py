#!/usr/bin/python3.7

'''
Displays sequence by turning the LED ON/OFF 
Recieves the following parameters
- fp: time per frame in seconds

- gpio_pins: gpio pins for each led connected to the RPi

- sequence: sequence of pixels used to display for particular LED
'''

import RPi.GPIO as GPIO
import time


def display(gpio_pins, sequence, fp = 1):
	#Input data to LED
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set up GPIO pins
	for j in gpio_pins:
		GPIO.setup(j, GPIO.OUT)

	# Activate according to sequence
	# Changed for Demo purposes
	for i in range(len(sequence[0])):
		for row, pin in enumerate(gpio_pins):
			print(sequence[row][i])
			if sequence[row][i]:
				GPIO.output(pin, GPIO.HIGH)
			else:
				GPIO.output(pin, GPIO.LOW)
		time.sleep(fp)

	# Turn LED off at the end
	for j in gpio_pins:
		GPIO.output(j, GPIO.LOW)

def display_off(gpio_pins):
	#Input data to LED
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	# Set up GPIO pins
	for j in gpio_pins:
		GPIO.setup(j, GPIO.OUT)

	# Turn LED off at the end
	for j in gpio_pins:
		GPIO.output(j, GPIO.LOW)
