#########
# Morphological Transformation are some simple operations based on the image shapes
# MT are normally performed on binary images
# Require 2 things
#  -> Original image
#  -> Structuring element / Kernel (decides the nature of the operations)
#      -> A Kernel tells you how to change the value of any given pixel by combining it with different amounts of the neighboring pixels
#########

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)

# work on binary images -> do mask, simple thresholding
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # apply erosion then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # apply dilation then erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel) # difference btw dilation & erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel) # difference btw opening and ori img

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range (len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()