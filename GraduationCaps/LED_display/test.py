#!/usr/bin/python3.7
from display_demo import *
from input_pixelator import *

data, data_width = input_pixelator(2, 2, "abc", "fonts/font.ttf")
print(data)
print(data_width)
sequences = assign_seq(data_width, 2, 2, data)
print(sequences)

