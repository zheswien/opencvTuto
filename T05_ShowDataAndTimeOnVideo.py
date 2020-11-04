import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3,1200) # 3-> Width
# cap.set(4,700) # 4 -》 height

# print(cap.get(3),cap.get(4))


while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: ' + str(cap.get(3)) + '   Height: ' + str(cap.get(4))
        date = str(datetime.datetime.now())

        frame = cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        frame = cv2.putText(frame,date,(10,90),font,1,(0,255,255),2,cv2.LINE_AA)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the capture var, release the resources
cap.release()
cv2.destroyAllWindows()

