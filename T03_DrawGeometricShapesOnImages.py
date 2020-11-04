import numpy as np
import cv2

# 2 Methods to read images
img = cv2.imread("lena.jpg",1)
# img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(0,0),(250,250),(255,0,0),4)
img = cv2.arrowedLine(img,(0,255),(255,255),(255,234,0),4)
img = cv2.rectangle(img,(100,100),(300,300),(2,234,0),4)
img = cv2.rectangle(img,(400,100),(600,300),(2,234,0),-1) # -1 = fill
img = cv2.circle(img,(447,63),50,(0,0,0),8)
img = cv2.circle(img,(147,63),50,(0,0,0),-1)

img = cv2.putText(img,'OpenCV',(5,500),cv2.FONT_HERSHEY_COMPLEX,4,(255,255,255),7,cv2.LINE_AA)

cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()