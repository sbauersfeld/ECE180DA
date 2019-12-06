#!/usr/bin/python3.7
from display_demo import *
from input_pixelator import *

data, data_width = input_pixelator(4, 5, "a", "fonts/font.ttf")
print(data)
print(data_width)
sequences = assign_seq(data_width, 5, 4, data)
print(sequences)
print(len(sequences))
display([14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21, 26, 19, 13, 6, 5, 11, 2, 22], sequences)

