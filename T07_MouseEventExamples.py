import numpy as np
import cv2

################## EXAMPLE 1 #####################
# # print events in the cv2 library
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
#
# # x & y coordinates
# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x, y), 3,(255,3,5),-1)
#         points.append((x,y))
#         if len(points) >= 2:
#             cv2.line(img,points[-1], points[-2], (92,45,123), 5)
#         cv2.imshow('image', img)
#
# img = np.zeros([512,512,3],np.uint8)
# # img = cv2.imread("lena.jpg",1)
# cv2.imshow('image',img)
# points = []
#
# cv2.setMouseCallback('image', click_event)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

################## EXAMPLE 2 ######################
####### Open a new window that shows the colour of the position clicked
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y ,0]
        green = img[x, y, 1]
        red = img[x , y, 2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        mycolorImage = np.zeros((512,512,3),np.uint8)

        # Fill the image in a new window with the colour
        mycolorImage[:] = [blue, green, red]
        cv2.imshow('colour', mycolorImage)

# img = np.zeros([512,512,3],np.uint8)
img = cv2.imread("lena.jpg",1)
cv2.imshow('image',img)
points = []

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()