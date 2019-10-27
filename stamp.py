from PIL import Image, ImageDraw  # Pillow library, for all image handling
from os import listdir  # To list files in a directory
from os.path import isfile, join  # Check if path is an actual file and join 2 paths together
from sys import argv  # For getting argument of files dragged

#-- Epic planning --#
# Steps for stamping

# Get design  -Done
# Get all tshirts and put them on a list -Done
# Make transparent -Done
# make a list with the design in each available colour, design_colours = []
# Resize each one
# for i in design_colour stamp i on all tshirts and save each file on final_tshirt folder
# print when each combination is finished

def remove_background(img): 
	"""This function takes an image as a parameter and checks for each pixel to know if its between a light gray or white.
	If it is then the function takes the pixel and makes it transparent (Alpha value = 0)."""
	
	data = img.getdata()  # Get data from picture
	new_data = []  # Set new list
	
	for item in data: # This checks if each pixel has a color like gray or darker
		if item[0] > 60 and item[0] > 60 and item[0] > 60:  
			new_data.append((255, 255, 255, 0))  # Adds a transparent pixel instead of white previous one
		else:
			new_data.append(item)  # Adds item without changing anything
	
	img.putdata(new_data)  # Applies the new data with transparent pixels to the old image
	return img

# Get design file name by argument. [0] is .py file name
designs = argv[1:]

if not designs:  # Check if design is empty ([] == False)
	print('Please provide at least one argument and make sure the file is in the same folder as this file')  # Error msg
	exit()
	
# Use list comprehension to run a for loop on all files in .\shirts and if its a file join paths then put into list
shirts = [f for f in listdir(r'.\shirts') if isfile(join(r'.\shirts', f))]  
	

# Use for loop to run design program per argument given
for i in designs:
	image = Image.open(i)  # Open picture using PIL
	no_background = remove_background(image)  # Remove background of each image
	
