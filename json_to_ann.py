import Utils
import numpy as np
from PIL import Image
import os

# Saves annotated image of number

jsonFile = "results/euler/54x66/prime_2020-05-11 213910.json"
imgFile = "ann_"+os.path.basename(jsonFile)+".png"

num, colors, size = Utils.load_from_file(jsonFile)
f = Utils.plot_number(num, colors, size, True, True)
f.savefig(imgFile, bbox_inches='tight')