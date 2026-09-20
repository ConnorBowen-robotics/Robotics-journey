import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print(f"can not open the camera :( ")
    exit()
while True:
    #reads video capture
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()