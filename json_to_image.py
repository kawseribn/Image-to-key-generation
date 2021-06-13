import Utils
import numpy as np
from PIL import Image
import os

# Saves image of prime

jsonFile = "./results/euler/54x66/prime_2020-05-11 213910.json"

imgFile = "img_"+os.path.basename(jsonFile)+".png"

# load from json
num, colors, size = Utils.load_from_file(jsonFile)

# rescale normalized RGB values to 0..255
colors = np.array(colors)*255

# convert num to array of digits
digits = list(map(int,str(num)))

# create rgb array from digits and colors
rgb_array = np.array([colors[d] for d in digits])

# create image
im = Image.frombytes("RGB", size, rgb_array.astype('uint8'))

# save
im.save(imgFile)