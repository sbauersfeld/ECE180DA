#!/usr/bin/python3.7
from PIL import Image, ImageDraw, ImageFont

def input_pixelator(width, height, set_font = "arial", set_scroll = False, message)
	font = ImageFont.truetype("fonts/" set_font + ".ttf", height)
	# 'W' is the width, it is calculated by the length of the message and add blank space if scrolling is desired
	scroll = 2
	if not set_scroll:
	    scroll = 0
	W, H = (font.getsize(message)[0] + scroll * width, height)

	im = Image.new("1", (W, H), 0)
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(message, font)
	draw.text(((W - w) / 2, (H - h) / 2 - h / 6), message, fill=1, font=font)

	# save image for testing
	im.save("msg_pixelator.png", "PNG")

	data = list(im.getdata())
	return data



