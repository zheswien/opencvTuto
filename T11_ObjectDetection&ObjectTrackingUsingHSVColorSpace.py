################# FILRER IMAGE COLOR ##################
# import cv2
# import numpy as np
#
# def nothing(x):
#     print(x)
#
# cv2.namedWindow('Tracking')
# cv2.createTrackbar('LH','Tracking', 0, 255, nothing)
# cv2.createTrackbar('LS','Tracking', 0, 255, nothing)
# cv2.createTrackbar('LV','Tracking', 0, 255, nothing)
# cv2.createTrackbar('UH','Tracking', 255, 255, nothing)
# cv2.createTrackbar('US','Tracking', 255, 255, nothing)
# cv2.createTrackbar('UV','Tracking', 255, 255, nothing)
#
# while(True):
#     img = cv2.imread("smarties.png")
#
#     hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
#     l_h = cv2.getTrackbarPos('LH','Tracking')
#     l_s = cv2.getTrackbarPos('LS','Tracking')
#     l_v = cv2.getTrackbarPos('LV','Tracking')
#     u_h = cv2.getTrackbarPos('UH','Tracking')
#     u_s = cv2.getTrackbarPos('US','Tracking')
#     u_v = cv2.getTrackbarPos('UV','Tracking')
#
#     # # Lower bound of blue colour
#     # l_b = np.array([88,111,49])
#     # # Upper bound of blue color
#     # u_b = np.array([130,255,255])
#
#     l_b = np.array([l_h,l_s,l_v])
#     u_b = np.array([u_h,u_s,u_v])
#
#     mask = cv2.inRange(hsv, l_b, u_b)
#
#     res = cv2.bitwise_and(img, img, mask=mask)
#
#     cv2.imshow('frame', img)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#
#     k = cv2.waitKey(1)
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()

####################### FILTER VIDEO COLOR ######################
import cv2
import numpy as np

def nothing(x):
    print(x)

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH','Tracking', 0, 255, nothing)
cv2.createTrackbar('LS','Tracking', 0, 255, nothing)
cv2.createTrackbar('LV','Tracking', 0, 255, nothing)
cv2.createTrackbar('UH','Tracking', 255, 255, nothing)
cv2.createTrackbar('US','Tracking', 255, 255, nothing)
cv2.createTrackbar('UV','Tracking', 255, 255, nothing)

while(True):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH','Tracking')
    l_s = cv2.getTrackbarPos('LS','Tracking')
    l_v = cv2.getTrackbarPos('LV','Tracking')
    u_h = cv2.getTrackbarPos('UH','Tracking')
    u_s = cv2.getTrackbarPos('US','Tracking')
    u_v = cv2.getTrackbarPos('UV','Tracking')

    # # Lower bound of blue colour
    # l_b = np.array([88,111,49])
    # # Upper bound of blue color
    # u_b = np.array([130,255,255])

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()