import cv2

# img = cv2.imread("lena.jpg",0)
# print(img)
#
# cv2.imshow('lena',img)
# cv2.imwrite('lena_copy.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.imread("lena.jpg",0)
cv2.imshow("image",img)
# & 0xFF for 64-bit
# waitkey(0) will not auto close the frame, close when click close window
k = cv2.waitKey(0) & 0xFF

# 27 -> ESC key
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'): # When press 's' key
    cv2.imwrite("lena_copy.jpg",img)
    cv2.destroyAllWindows()