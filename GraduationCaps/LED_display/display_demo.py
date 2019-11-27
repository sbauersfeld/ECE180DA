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

	for j in gpio_pins:
		GPIO.setup(j, GPIO.OUT)

	for i in range(len(sequence[0])):
		for j in range(len(gpio_pins))
			if sequence[j][i] == 1:
				GPIO.output(gpio_pins[j], GPIO.HIGH)
			else:
				GPIO.output(gpio_pins[j], GPIO.LOW)
			time.sleep(fp)

	# Turn LED off at the end
	for j in gpio_pins:
		GPIO.output(j, GPIO.LOW)
