###############
# Canny edge -> An edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.
# Composed of 5 stages:
#  - Noise reduction
#  - Gradient calculation
#  - Non-maximum suppression (Edge detection)
#  - Double threshold (Find potential edges)
#  - Edge tracking by hysteresis
###############

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg', 0)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'canny']
images = [img, canny]

for i in range (len(images)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()