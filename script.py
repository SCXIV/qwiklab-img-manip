#!/usr/bin/env python3

import os
import PIL
import pathlib
from PIL import Image
from pathlib import Path

directory = 'images'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        trimmed_name = Path(filename).stem
        try:
            original_img = Image.open(f)
            original_img.rotate(90).resize((128, 128)).save("images/changed_images/{}.jpeg".format(filename))
        except IOError as e:
            print(e)