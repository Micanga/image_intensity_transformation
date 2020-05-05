"""
- name: Matheus Aparecido do Carmo Alves
- usp number: 9791114
- course code: SCC0251
- year/semester: 2020/1
- github repo: https://github.com/Micanga/image_intensity_transformation

- title of the assignment:
Assignment 1: Image Intensity Transformation
"""
import imageio
import numpy

#####
# SUPPORT VARIABLES
#####
INVERSION   = 1
CONTRAST    = 2
LOGARITHMIC = 3
GAMMA		= 4

#####
# IMAGE PROCESSING METHODS
#####
def inversion(input_img):
	# 1. Creating the output image
	width, height = input_img.shape
	output_img = numpy.zeros((width,height))

	# 2. Performing the image inversion
	for i in range(width):
		for j in range(height):
			# - getting the pixel
			pixel = input_img[i,j]

			# - applying the inversion
			new_value = 255 - pixel

			# - setting it in the output image
			output_img[i,j] = new_value

	# 3. Returning the result image
	return output_img

def contrast_modulation(input_img):
	# 1. Creating the output image
	width, height = input_img.shape
	output_img = numpy.zeros((width,height))

	# 2. Reading the constants for contrast
	# -- a: lowest image intensity
	# -- b: highest image intensity
	# -- c: new lowest image intensity
	# -- d: new highest image intensity
	a = int(numpy.min(input_img))
	b = int(numpy.max(input_img))
	c = int(input())
	d = int(input())

	# 3. Performing the contrast modulation
	for i in range(width):
		for j in range(height):
			# - getting the pixel
			pixel = input_img[i,j]

			# - applying the contrast modulation
			new_value = (pixel-a)*((d-c)/(b-a)) + c

			# - setting it in the output image
			output_img[i,j] = float(new_value)

	# 4. Returning the result image
	return output_img

def logarithmic_function(input_img):
	# 1. Creating the output image
	width, height = input_img.shape
	output_img = numpy.zeros((width,height))

	# 2. Reading the constants for contrast
	# -- R: highest image intensity
	R = numpy.max(input_img)

	# 3. Applying the logarithmic function
	for i in range(width):
		for j in range(height):
			# a. getting the pixel
			pixel = input_img[i,j]

			# b. applying the inversion
			new_value = 255*numpy.log2(1+pixel)/numpy.log2(1+R)

			# c. setting it in the output image
			output_img[i,j] = float(new_value)

	# 4. Returning the result image
	return output_img

def gamma_adjustment(input_img):
	# 1. Creating the output image
	width, height = input_img.shape
	output_img = numpy.zeros((width,height))

	# 2. Reading the constants for contrast
	W = int(input())
	lambd = float(input())

	# 3. Performing the gamma adjustment
	for i in range(width):
		for j in range(height):
			# - getting the pixel
			pixel = input_img[i,j]

			# - applying the gamma adjustment
			new_value = W*(pixel**lambd)

			# - setting it in the output image
			output_img[i,j] = float(new_value)

	# 4. Returning the result image
	return output_img

#####
# METRIC METHOD
#####
def RSE(input_img,output_img):
	RSE = 0.0
	width, height = input_img.shape
	for i in range(width):
		for j in range(height):
			RSE += (output_img[i,j] - float(input_img[i,j]))**2
	RSE = numpy.sqrt(RSE)
	return RSE

#####
# MAIN CODE
#####
# 1. Reading the inputs
# a. image
filename = str(input()).rstrip()
input_img = imageio.imread(filename)

# b. desired method
method = int(input())
save = int(input())

# 2. Starting the image processing
# a. Inversion
# T(i) = 255 - i
if method == INVERSION:
	output_img = inversion(input_img)

# b. Contrast modulation
# T(i) = (i-a)*((d-c)/(b-a)) + c
elif method == CONTRAST:
	output_img = contrast_modulation(input_img)

# c. Logarithmic function
# T(i) = 255*log2(1+i)/log2(1+R)
elif method == LOGARITHMIC:
	output_img = logarithmic_function(input_img)

# d. Gamma adjustment
# T(i) = W*i**lambd
elif method == GAMMA:
	output_img = gamma_adjustment(input_img)

# e. Invalid method
else:
	print('InputError: invalid input method (integer between 1 and 4).')
	exit(1)

# 3. Saving the image (if requested)
if save == 1:
	imageio.imwrite('output_img.png',output_img.astype(numpy.uint8))

# 4. Caculating the RSE
RSE = RSE(input_img,output_img)
print('%.4f' % RSE)

# That's all folks... :}