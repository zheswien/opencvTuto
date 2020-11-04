#######################
# Contour 轮廓-> the curve joining all the continuous point along the boundary which has the same colour or intensity
# -> useful tool for shape analysis / object detection / object recognition
# -> Use binary image to find the contour for better accuracy
# 1. generate binary image
# 2. Apply threshold/canny edge detection
# 3. Find contours
#######################

import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 100, 255, 0)

# contour -> a python list of all the countours in the image. Each individual contour is a Numpy array of (x, y) coodinates of boundary points of the obj
# hierarchy -> Optional output vector which is containing the informaion about img topology
contours, hierarchy = cv2.findConstours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours: " + str(len(contours)))
print(contours[0])

# cv2.drawContours(img, contours, -1, (0, 255 , 0), 3) # 0 -> Draw the first contour (If num of contours = 8, can put 0 - 7 & -1)
cv2.drawContours(img, contours, -1, (0, 255 , 0), 3) # -1 -> Draw all contours

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()