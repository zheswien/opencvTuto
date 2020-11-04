import numpy as py
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape)    # returns a tuple of number of rows, columns, and channels
print(img.size) # Total number of pixels is accessed
print(img.dtype)    # Image data type

b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
# cv2.imshow('ball',ball)
img[273:333, 100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# dst = cv2.add(img,img2)
# dst = cv2.addWeighted(img,0.9,img2,0.1,0)
dst = cv2.addWeighted(img,0.2,img2,0.8,0)

# cv2.imshow('image',img)
cv2.imshow('add',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
