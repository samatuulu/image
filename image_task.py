#!/usr/bin/env python
import os, fnmatch
from PIL import Image, ImageDraw, ImageFont


file_name = fnmatch.filter(os.listdir('/home/beka/Desktop/source-images'), '*.jpg')
output_images = '/home/beka/Desktop/source-images/output-images/'

output_file = 'test.jpg'

i = 1

for image in file_name:
	remove_character = '.jpg'
	removed = image.split(remove_character, 1)[0]

	images = '/home/beka/Desktop/source-images/' + image

	image = Image.open(images)
	font_type = ImageFont.load_default()
	draw = ImageDraw.Draw(image)
	draw.text(xy=(600,550), text='@' + removed, fill=(255,69,0), font=font_type)
	i += 1
	output_image_name = str(i) + output_file
	file_path = os.path.join(output_images, output_image_name)
	image.save(file_path)
