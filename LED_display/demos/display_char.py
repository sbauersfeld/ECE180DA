#!/usr/bin/python3.7
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
import time

# Delay in seconds
wait = 5

# Enter dimensions and message
width = int(input("Enter width: "))
height = int(input("Enter height: "))
message = input("Enter message: ")
W, H = (width, height)

# Draw text and output pixel data
im = Image.new("1", (W, H), 0)
font = ImageFont.truetype("arial.ttf", 10)
draw = ImageDraw.Draw(im)
w, h = draw.textsize(message, font)
draw.text(((W-w)/2, (H-h)/2 - h/6), message, fill=1, font=font)
im.save("char_pixelator.png", "PNG")
data = list(im.getdata())
print(data)

#Input data to LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enter LEDs corresponding GPIO pins
LED = [int(i) for i in input("Enter GPIO pins: ").split()]
for i in LED:
	GPIO.setup(i, GPIO.OUT)

# If the pixel is painted, turn on the corresponding LED
for i in range(len(data)):
	if data[i] == 1:
		GPIO.output(LED[i], GPIO.HIGH)

time.sleep(wait)

# Turn off LEDs
for i in LED:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)




