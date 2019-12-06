#!/usr/bin/python3.7
from PIL import Image, ImageDraw, ImageFont

def input_pixelator(width, height, message, set_font, set_scroll = True):
	font_size = height // 10 * 10 + 10 
	font = ImageFont.truetype(set_font, font_size)

	# 'W' is the width, calculated by the length of the message
	# Add blank space if scrolling is desired
	scroll = 2 # doesn't this need to be just 1?
	if not set_scroll:
	    scroll = 0
	W, H = (font.getsize(message)[0] + scroll * width, height)

	# Draw Image
	im = Image.new("1", (W, H), 0)
	draw = ImageDraw.Draw(im)
	w, h = draw.textsize(message, font)
	draw.text(((W - w) / 2, (H - h) / 2 - h / 4), message, fill=1, font=font)

	# Save image for testing
	im.save("msg_pixelator.png", "PNG")

	data = list(im.getdata())
	return data, W

def assign_seq(data_width, rows, columns, data):
	sequences = []
	for i in range(rows):
		for j in range(columns):
			# shouldn't this be just (...data_width - columns)?
			seq = data[i * data_width + j: i * data_width + j + data_width - (columns - 1)]
			sequences.append(seq)
	return sequences
