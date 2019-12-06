#!/usr/bin/python3.7
from display_demo import *
from input_pixelator import *

data, data_width = input_pixelator(4, 5, "UCLA", "fonts/font.ttf")
print(data)
print(data_width)
sequences = assign_seq(data_width, 5, 4, data)
print(sequences)
print(len(sequences))
display([2, 3, 14, 15, 4, 17, 18, 23, 27, 22, 24, 25, 10, 9, 8, 7, 11, 5, 12, 16], sequences, fp=0.5)

