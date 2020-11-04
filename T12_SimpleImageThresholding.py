import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('gradient.png',0)
# If the value of the pixel is less than 127 -> 0 (black) else 1 (white)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_MASK)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_OTSU)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th6 = cv.threshold(img, 127, 255, cv.THRESH_TRIANGLE)
_, th7 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

title = ['Ori Image', 'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_MASK', 'THRESH_OTSU', 'THRESH_TOZERO', 'THRESH_TRIANGLE', 'THRESH_TRUNC']
images = [img, th1, th2, th3, th4, th5, th6, th7]

for i in range (len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
# cv.imshow('Image', img)
# cv.imshow('th1', th1)
# cv.imshow('th2', th2)
# cv.imshow('th3', th3)
# cv.imshow('th4', th4)
# cv.imshow('th5', th5)
# cv.imshow('th6', th6)
# cv.imshow('th7', th7)


cv.waitKey(0)
cv.destroyAllWindows()