import cv2

# capture livestream from cam

# can write a filename or provide index num of the cam you want to read (0/-1) (1/2 for 2nd or 3rd cam)
# cap = cv2.VideoCapture('movie.mp4/avi')
cap = cv2.VideoCapture(0)

# FourCC Code
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# save the output (format, fourcc code, frame/sec, frame height & width)
out = cv2.VideoWriter('audio.avi',fourcc,20.0,(640,480))
print(cap.isOpened())

# run infinity to capture the frame
# while(True):

while(cap.isOpened()):
    # ret return true if the frame is available, fame var will capture and save the frame
    ret, frame = cap.read()

    if ret == True:
        # Get some properties of the frame using get
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        # Convert to grayscale
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # Display
        cv2.imshow('Video', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release the capture var, release the resources
cap.release()
out.release()
cv2.destroyAllWindows()

