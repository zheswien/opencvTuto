####################
# An image gradient is a directional change in the intensity or color in an image
####################

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F) # a datatype which is 64bit float & supports -ve numbers which will be dealing with when lap method is run on the img
lap2 = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
# take absolute value of the laplacian image transformation, convert this value back to the unsigned 8-bit integer which is suitable for the output
lap = np.uint8(np.absolute(lap))
lap2 = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #order of derivative x & y
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombine = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'laplacian', 'laplacian with kernel', 'SobelX', 'SobelY', 'sobelCombine']
images = [img, lap, lap2, sobelX, sobelY, sobelCombine]

for i in range (len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()