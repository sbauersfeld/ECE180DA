#!/usr/bin/python3.7
from display_demo import *
from input_pixelator import *

data, data_width = input_pixelator(2, 2, "what the hell", "fonts/font.ttf")
print(data)
print(data_width)
sequences = assign_seq(data_width, 2, 2, data)
print(sequences)
display([15, 14, 23, 18], sequences, fp=0.5)

