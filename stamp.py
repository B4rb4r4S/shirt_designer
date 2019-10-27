from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together
from sys import argv  # For getting argument of files dragged

# Get design file name by argument. [0] is .py file name
design = argv[1:]

if design:  # Check if design is empty
    print('Please provide at least one argument')
    exit()
# Use for loop to run design program per argument given
for i in design:
    pass
