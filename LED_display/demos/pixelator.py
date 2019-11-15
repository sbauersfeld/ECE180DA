#!/usr/bin/python3.7
from PIL import Image, ImageDraw, ImageFont

# With prompts
width = int(input("Enter width: "))
height = int(input("Enter height: "))
message = input("Enter message: ")
W, H = (width, height)

# No prompts
'''
W, H = (10, 10)
message = "q"
'''

im = Image.new("1", (W, H), 0)
font = ImageFont.truetype("arial.ttf", 10)
draw = ImageDraw.Draw(im)
w, h = draw.textsize(message, font)
draw.text(((W-w)/2, (H-h)/2 - h/6), message, fill=1, font=font)

im.save("char_pixelator.png", "PNG")
data = list(im.getdata())
print(data)


