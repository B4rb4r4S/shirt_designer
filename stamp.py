from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together
from sys import argv  # For getting argument of files dragged

#-- Epic planning --#
# Steps for stamping

# Get design 
# Get all tshirts and put them on a list
# Make transparent
# Resize
# make a list with the design in each available colour, design_colours = []
# for i in design_colour stamp i on all tshirts and save each file on final_tshirt folder
# print when each combination is finished


# Get design file name by argument. [0] is .py file name
design = argv[1:]

if not design:  # Check if design is empty ([] == False)
	print('Please provide at least one argument')  # Error msg
	exit()
	
# Use list comprehension to run a for loop on all files in .\shirts and if its a file join paths then put into list
shirts = [f for f in listdir(r'.\shirts') if isfile(join(r'.\shirts', f))]  
	
	
# Use for loop to run design program per argument given
for i in design:
	pass