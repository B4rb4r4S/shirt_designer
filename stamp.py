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
#	 Nested for loop in a for loop to cycle between colour_list and pixels
#	 If item[4] != 0: etc. If its not transparent do thing
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

def black_to_colour(img, colour_list):
	data = img.getdata()  # GEt data etc
	new_data = []  # SAme first steps as remove_background()
	
	img_width, img_height = img.size  # Get size of design sent and store in varibles
	
	colour_designs = []  # Where all the finished images go. 
	
	for colour in colour_list:  # For each colour change the colour in the image
	
		print(f'Changing design colour to {colour[1]}')
		for item in data:  # Now doing for each pixel
			
			if item[3] != 0:  # if the pixel is not transparent change the colour
				new_data.append(colour[0])
				
			else:
				new_data.append(item)
				
		
		print(len(new_data), 'New')
		print(len(data), 'Old')
		
		# After colour change is complete a new image with same size is created
		new_design = Image.new('RGBA', (img_width, img_height), (255, 255, 255, 0))
		# And the data is put into it
		new_design.putdata(new_data)   #--------------- NOT WORKING, when it gets to black it duplicates the pixels. 
		# fix!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		
		new_design.show()
		
		colour_designs.append((new_design, colour[1]))  # To list add new image + colour name
		
	return colour_designs
	
#-- Design colours with rgba values and names --#
colours = [
((240, 10, 10, 1), 'red'), 
((0, 0, 0 , 1), 'black'), 
((255, 255, 255, 1), 'white'), 
((237, 170, 14, 1), 'gold'), 
((247, 123, 7, 1), 'orange'), 
((250, 250, 0, 1), 'yellow')
]
	
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
	
	design_colour_list = black_to_colour(no_background, colours)
	design_colour_list[1][0].show()
