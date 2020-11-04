#######################
# Image Pyramid / Pyramid representation
# -> A type of multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling
# -> 2 types
#    -> Gaussian pyramid (Repeat filtering and subsampling the image)
#        -> 2 functions: Pair down & Pair up
#    -> Laplacian pyramid (are from Gaussian Pyramids, no exclusion function)
#        -> A lvl in LPyr is formed by the diff btw that lvl in GPyr & expanded ver. of its upper lvl in GPyr
#
# !! Benefits: Helps to blend and reconstruct the images
#######################
import cv2
import numpy as np

################# Gaussian Pyramid ################
# img = cv2.imread('lena.jpg')
# #lower resolution (abt 1/4 of the ori img)
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# #higher resolution
# hr1 = cv2.pyrUp(lr2)
#
# cv2.imshow('Original image', img)
# cv2.imshow('PyrDown1 image', lr1)
# cv2.imshow('PyrDown2 image', lr2)
# cv2.imshow('PyrUp1 image', hr1)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

################ Laplacian Pyramid ################
img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range (6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('Upper lvl GP', layer)
lp = [layer]

for i in range (5, 0, -1): # Decreasing from 5 to 1
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)


cv2.imshow('Original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()