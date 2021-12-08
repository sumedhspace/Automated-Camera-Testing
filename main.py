import cv2
import numpy

#capturing video input from first webcam
capture = cv2.VideoCapture(0)

i=0
while(capture.isOpened() and i < 1 ):
    success , img = capture.read() 
    cv2.imwrite("test_case"+str(i)+".jpeg",img)
    i+=1

capture.release()




# #PERSONAL NOTES
# Extract the image pixel array - Scan through the array using 64x64 windows; for each window, calculate the texture features, store them into arrays - Study the histogram(s) you obtained from the image feature array