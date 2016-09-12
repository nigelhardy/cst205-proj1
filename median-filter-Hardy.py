'''
load in 9 images
save 9 pixels, one pixel from each
use one channel to get median
rewrite that pixel into new image

Github link
https://github.com/nigelhardy/cst205-proj1
'''
from PIL import Image

import sys

class pixel(object):
    def __init__(self, r, g, b):
        """Set pixel colors"""
        self.r = r
        self.g = g
        self.b = b

if len(sys.argv) == 2:
	numOfImages = int(sys.argv[1])
else:
	numOfImages = 9

#numOfImages = 9

fileList = [1,2,3,4,5,6,7,8,9] #filenames array
imageList = [None] * numOfImages

for x in range(0, numOfImages):
    fileList[x] = 'Project1Images/' + str(x + 1) + '.png' #creating 9 filenames

#imageList = [1,2,3,4,5,6,7,8,9] #array for 9 images loaded in
imageList = [None] * numOfImages


for x in range(0, numOfImages): #opening files from filename array
	imageList[x] = Image.open(fileList[x])
	imageList[x].load()


newImage = imageList[0] #this will be the filtered image

'''for x in range(0, 9):
	print "The size of the Image is: "
	print(imageList[x].format, imageList[x].size, imageList[x].mode)'''

for x in range(0, imageList[0].size[0]):
	for y in range(0, imageList[0].size[1]):
		#pixValues = [1,2,3,4,5,6,7,8,9] #nine temporary values of pixel from each photo
		pixValues = [None] * numOfImages
		for z in range(0, numOfImages):
			pixTemp = imageList[z].getpixel((x, y)) #get pixel values
			#r, g, b, a = pixTemp
			pixValues[z] = pixel(pixTemp[0],pixTemp[1],pixTemp[2]) #store pixel for sorting
		pixValues.sort(key = lambda x: x.r) #sort by red channel
		newImage.putpixel((x,y),(pixValues[int(numOfImages/2)].r, pixValues[int(numOfImages/2)].g, pixValues[int(numOfImages/2)].b)) #put median pixel into new image
print("Done!")
newImage.show()
newImage.save("Project1Images/medianFilteredImage.png") #save new image