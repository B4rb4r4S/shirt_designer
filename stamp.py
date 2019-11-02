from PIL import Image, ImageDraw, ImageOps  # Pillow library, for all image handling
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
		if item[0] > 60 and item[1] > 60 and item[2] > 60:  
			new_data.append((255, 255, 255, 0))  # Adds a transparent pixel instead of white previous one
		else:
			new_data.append(item)  # Adds item without changing anything
	
	img.putdata(new_data)  # Applies the new data with transparent pixels to the old image
	return img

def black_to_colour(img, colour_list):
	data = img.getdata()  # GEt data etc
	
	img_width, img_height = img.size  # Get size of design sent and store in varibles
	
	colour_designs = []  # Where all the finished images go. 
	
	for colour in colour_list:  # For each colour change the colour in the image
	
		print(f'Changing design colour to {colour[1]}')
		
		new_data = []  # clean variable
		
		for item in data:  # Now doing for each pixel
			
			if item[3] != 0:  # if the pixel is not transparent change the colour
				new_data.append(colour[0])
				
			else:
				new_data.append(item)  # if not put the pixel back
		
		# After colour change is complete a new image with same size is created
		new_design = Image.new('RGBA', (img_width, img_height), (255, 255, 255, 0) )
		# And the data is put into it
		new_design.putdata(new_data)
		
		colour_designs.append((new_design, colour[1]) )  # To list add new image + colour name
		
	return colour_designs
	
def resize(image):
	# Get size desired, if size too big the default to 390 px
	try:
		percentage = int(input('% used by design vertically: '))  # Ask for percentage of tshirt occupied vertically
	except ValueError:
		print('Please only enter a number')
	
	raw_width, raw_height = image.size  # Gets size for first image
	
	decimal_percentage = percentage/100  # Get number inputed as a decimal eg: 0.65
	new_height = int(770 * decimal_percentage)  # Get percentage of full tshirt vertical size (770)
	new_width = round((raw_width * new_height) / raw_height)  # Use previous value to get the new size without changin the ratio

	if new_width > 390:  # 390 is the maximum width of tshirt
		print('Width too big, setting to max...')
		new_width = 390 # Maximum width
		new_height = round((raw_height * new_width) / raw_width) # Use previous value to get the new size without changin the ratio
	
	resized_design = image.resize((new_width, new_height) )
	
	return resized_design
	
def stamp(shirt_list, design_list):
	
	# create variable where shirt colour and design colour [[stamped shirt, 'blue shirt yellow design'], etc] is going to be appended 
	final_shirts_list = []
	
	# Create a mask from white design
	design_mask = design_list[0][0].convert('1')
	
	# For each tshirt stamp each design - for i in tshirt : for j in design
	for shirt in shirt_list:
		
		# Open shirt from folder as an image object
		shirt_img = Image.open(f'shirts\\{shirt}')
		
		shirt_img = shirt_img.convert('RGB')
		
		# Get size of shirt
		shirt_width, shirt_height = shirt_img.size
		
		for design in design_list:
			
			# Get size
			design_width, design_height = design[0].size
			
			# GEt image from list
			design_img = design[0]
			design_img = design_img.convert('RGB')
			
			
			# Create a white canvas size of shirt
			final_shirt = Image.new('RGB', (shirt_width, shirt_height), (255, 255, 255, 1) )
			
			# paste shirt into canvas
			final_shirt.paste(shirt_img, (0, 0) )
			
			# paste design in the middle 237px from the top (armpit line)
			final_shirt.paste(design_img, (round(shirt_width / 2  -  design_width / 2), 237), mask = design_mask)
			
			# Generate shirt name
			shirt_name = shirt[:-4] + ' shirt with ' + design[1]
			
			# Add to list the image and the name
			final_shirts_list.append([final_shirt, shirt_name])
	
		# Tell user current finished tshirt. [:-3] to exclude extension
		print(f'{shirt[:-4]} shirts have been finished.')
	# return variable
	return final_shirts_list
	
#-- Design colours with rgba values and names --#
colours = [
((255, 255, 255, 1), 'white'),
((0, 0, 0 , 1), 'black'),
((240, 10, 10, 1), 'red'), 
((237, 170, 14, 1), 'gold'), 
((235, 107, 52, 1), 'orange'), 
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
	image = image.convert('RGBA')
	
	
	no_background = remove_background(image)  # Remove background of image
	
	new_size_design = resize(no_background)  # Resize image
	
	final_designs = black_to_colour(new_size_design, colours)  # Change colour of image and store in list -> [[Image, 'red'], etc]
	
	finished_shirts = stamp(shirts, final_designs)  # Send to put the designs in
	
	# Save the images
	for image in finished_shirts:
	
		image[0].save(f'final_shirts\\{image[1]}.png')
	
