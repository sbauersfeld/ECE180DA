#!/usr/bin/python3.7

'''
Displays sequence by turning the LED ON/OFF 
Recieves the following parameters

- width: width of LED display

- height height of LED display

- position: position of LED display (calculated by row * column + column)

- fp: time per frame in seconds

- gpio_pins: gpio pins for each led connected to the RPi

- sequence: sequence of pixels used to display for particular LED
'''

import RPi.GPIO as GPIO
import time


def display(width, height, position, fp = 1, gpio_pin, sequence)
	GPIO.setup(gpio_pin, GPIO.OUT)

	for i in sequence:
		if i == 1:
			GPIO.output(gpio_pin, GPIO.HIGH)
			time.sleep(fp)
		else:
			GPIO.output(gpio_pin, GPIO.LOW)
			time.sleep(fp)

	# Turn LED off at the end
	GPIO.output(gpio_pin, GPIO.LOW)