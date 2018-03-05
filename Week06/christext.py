import requests
import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont



def write_text(imgfilename, text):
	im = Image.open(imgfilename)
	canvas = ImageDraw.Draw(im)
#	canvas.rectangle([0, 125, im.size[0], 166], fill=(0,0,0))
	fnt = ImageFont.truetype('/Library/Fonts/Butler_Bold.otf', 170)
	canvas.text((200, 800), text, font=fnt, fill=(255, 255, 0))
	im.save(imgfilename + '.modified.jpg')


write_text('chrisvanallsburg3.jpg', 'Chris Van Allsburg')

