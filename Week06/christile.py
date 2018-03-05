import glob
from PIL import Image
import random

blank_image = Image.new('RGB', (2200, 1900), (255, 255, 255))
blank_image.save('white.jpg')

# grap all the *.jpg files in 'babies' folder
jpegs = glob.glob('pinterest/*.jpg')

x=0
y=0

for jpg in jpegs:
	# print jpg
	im = Image.open(jpg)
	im.thumbnail((200, 200))
	w = im.size[0]
	h = im.size[1]
	blank_image.paste(im, (x, y))

	x += w
	if x>2000:
		x=0
		y+=h


blank_image.save('chrisvanallsburg3.jpg')
