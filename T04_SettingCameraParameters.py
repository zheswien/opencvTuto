import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Setting cam parameters
cap.set(3,1200) # 3-> Width
cap.set(4,700) # 4 -》 height

print(cap.get(3),cap.get(4))


while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the capture var, release the resources
cap.release()
cv2.destroyAllWindows()

