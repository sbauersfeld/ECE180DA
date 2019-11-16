#!/usr/bin/python3.7
from PIL import Image, ImageDraw, ImageFont

# set scroll to 2 if scrolling text is desired, else set it as 0
scroll = 2

# With prompts
'''
width = input("Enter width: ")
height = input("Enter height: ")
message = input("Enter message: ")

'''
# No prompts
width = 3
height = 3

message = "abc"
font = ImageFont.truetype("arial.ttf", height)

# 'W' is the width, it is calculated by the length of the message and add blank space if scrolling is desired

# No prompts
W, H = (font.getsize(message)[0] + scroll * width, height)

# With prompts
# W, H = (font.getsize(message)[0] + scroll * int(width), int(height))

im = Image.new("1", (W, H), 0)
draw = ImageDraw.Draw(im)
w, h = draw.textsize(message, font)
draw.text(((W-w)/2, (H-h)/2 - h/6), message, fill=1, font=font)

im.save("text_pixelator.png", "PNG")
data = list(im.getdata())
print(data)