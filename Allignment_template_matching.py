"""
This script is meant to check test an image for allignment
It takes the image captured in the main file and uses template matching to find the position of the symbol in target image 1.
Th escript will check for allignment by cheking the variance between the position of target symbol between the original image and the camera capture.
The threshhold is set to 5 pixels lengthwise and width wise. 
"""
import cv2


#importing the source image and the template 
#source image is the capture from the camera
#template is the symbol
source = cv2.imread('image.jpg')
template = cv2.imread('Template.png')

#display the image preview
#the imshow function takes two inputs, the name of the window and the object to display from
cv2.imshow('Preview', source)
cv2.waitKey(0)  

#converting to grayscale to make template matching easy 
#the cvtColor function used to convert from RGB to greyscale takes 2 parameters as input, 
# 1) object to apply color change
# 2)the color space conversion code 
source = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY) 

#Preview image in greyscale
cv2.imshow('Preview Greyscaled', source)
cv2.waitKey(0)  

#capturing the height and width
height, width =source.shape
height, width 

H, W = template.shape
H, W 

#a list of all the methods to see results from all the methods
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
method_sq = [cv2.TM_SQDIFF]

#main loop
for method in method_sq:
  #this loop goes through all the methods of template matching and produces a result for all of them
  src2 = source.copy()
  result = cv2.matchTemplate(src2, template, method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
  print(min_loc, max_loc)
  if method in [cv2.TM_SQDIFF,cv2.TM_CCORR]:
    location = min_loc
  else:
    location = max_loc
  bottom_right = (location[0] + W, location[1] + H)
  cv2.rectangle(src2, location,bottom_right, 0, 5)
  cv2.imshow('Template matched',src2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

x_diff = 269-min_loc[0]
y_diff = 177-min_loc[1]
if min_loc == (269,183):
    print("image is alligned")
else:
    print("Not alligned")
print(location)


