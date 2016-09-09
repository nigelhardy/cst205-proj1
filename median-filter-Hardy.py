'''
load in 9 images
save 9 pixels, one pixel from each
use one channel to get median
rewrite that pixel into new image

Github link
https://github.com/nigelhardy/cst205-proj1
'''
from PIL import Image

class pixel(object):
    def __init__(self, r, g, b):
        """Set pixel colors"""
        self.r = r
        self.g = g
        self.b = b

fileList = [1,2,3,4,5,6,7,8,9] #filenames array

for x in range(0, 9):
    fileList[x] = 'Project1Images/' + str(x + 1) + '.png' #creating 9 filenames

imageList = [1,2,3,4,5,6,7,8,9] #array for 9 images loaded in

for x in range(0, 9): #opening files from filename array
	imageList[x] = Image.open(fileList[x])
	imageList[x].load()


newImage = imageList[0] #this will be the filtered image

'''for x in range(0, 9):
	print "The size of the Image is: "
	print(imageList[x].format, imageList[x].size, imageList[x].mode)'''

for x in range(0, imageList[0].size[0]):
	for y in range(0, imageList[0].size[1]):
		pixValues = [1,2,3,4,5,6,7,8,9] #nine temporary values of pixel from each photo
		for z in range(0, 9):
			r, g, b = imageList[z].getpixel((x, y)) #get pixel values
			pixValues[z] = pixel(r,g,b) #store pixel for sorting
		pixValues.sort(key = lambda x: x.r) #sort by red channel
		newImage.putpixel((x,y),(pixValues[4].r, pixValues[4].g, pixValues[4].b)) #put median pixel into new image
print("Done!")
newImage.show()
newImage.save("Project1Images/medianFilteredImage.png") #save new image