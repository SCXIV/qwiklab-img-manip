#!/usr/bin/env python3

import os
import PIL
from PIL import Image

im = Image.open("images/image.jpg")
directory = 'images'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        try:
            original_img = Image.open(f)
            original_img.rotate(90).resize((128, 128)).save("images/changed_images/{}.jpeg".format(filename))
        except IOError as e:
            print(e)