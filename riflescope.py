#Importing necessary packages.
import cv2
import numpy as np

#Loading our input Image and displaying it.
image = cv2.imread("riflescope.png")
cv2.imshow('image', image)
cv2.waitKey(0)

#Converting it into grayscale and smoothing it (blurring it) to reduce high frequency noise.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow('image', blurred)
cv2.waitKey(0)

#Applying Thresholding
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('image', thresh)
cv2.waitKey(0)

#Performing series of erosion and dilations to get rid of noise.
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)
cv2.imshow('image', thresh)
cv2.waitKey(0)

#Getting edge pixel values to see if the image is Riflescoped or not
pixel = thresh

#Drawing a filled white rectangle in the center of the image to get the edge values 
start_point = (30, 30) 
end_point = (454, 296) 
color = (255, 255, 255)
thickness = -1
# Using cv2.rectangle() method 
pixel = cv2.rectangle(pixel, start_point, end_point, color, thickness) 

#Displaying the drawn rectangle
cv2.imshow('image', pixel)
cv2.waitKey(0)

#Printing Final Output that is if the Image is Riflescoped or not.
black_pix = np.sum(pixel == 0)  #getting number of black pixels 

if(black_pix > 100):
    print("Camera Rejected due to image being riflescoped.")
else: 
    print("Riflescope test passed...")
