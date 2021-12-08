#Importing necessary packages.
import cv2
import numpy as np

#Loading our input Image and displaying it.
image = cv2.imread("blackdot.png")
cv2.imshow('image', image)
cv2.waitKey(0)

#Inverting Image and displaying it
image = cv2.bitwise_not(image)
cv2.imshow('image', image)
cv2.waitKey(0)

#Converting it into grayscale and smoothing it (blurring it) to reduce high frequency noise.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow('image', blurred)
cv2.waitKey(0)

#Applying Thresholding
thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('image', thresh)
cv2.waitKey(0)

#Performing series of erosion and dilations to get rid of small blobs.
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)

#Printing Final Image
cv2.imshow('image', thresh)
cv2.waitKey(0)

#Printing Final Output that is if the Image contains blackspots or not.
pixel = thresh
white_pix = np.sum(pixel == 255)  #getting number of white pixels in the image which are blackspots

if(white_pix > 100):
    print("Camera Rejected due to blackspots in the Image.")
else: 
    print("Blackspot test passed...")S