#!/usr/bin/env python3

import os
import PIL
from PIL import Image

im = Image.open("image.jpg")
# new_im = im.resize((640,480))
# new_im.save("example_resize.jpg")

im.rotate(180).resize((1280,1024)).save("flip_resize.jpg")
print(im.format, im.size)