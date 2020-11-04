#################
# Homogeneous filter is the most simple filter, each output pixel is the mean of its kernel neighbors.
# In image processing, a kernel, convolution matrix, or mask is a small matrix.
# It is used for blurring, sharpening, embossing, edge detection, and more.
# Gaussian filter is nothing but using different-weight-kernel, in both x and y direction
# Median filter -> replace each pixel's value with the median of it's neighbouring pixels.
#     This method is great when dealing with 'salt and pepper noise'
#################

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('opencv-logo.png')
# img = cv2.imread('water.png')
img = cv2.imread('lena.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 4)
median = cv2.medianBlur(img, 5)
                                        # diameter of each pixel neighbourhood
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75) # Effective in removing noises while keeping the edge sharp


titles = ['image', '2D Convolution', 'blur', 'Gaussian B', 'Median B', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range (len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()