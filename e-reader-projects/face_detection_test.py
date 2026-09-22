import mediapipe as mp
import cv2 as cv
import time

cap = cv.VideoCapture(0)

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = "/home/vooddoo/projects/robotics-journey/e-reader-projects/face_landmarker.task"

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO)

with FaceLandmarker.create_from_options(options) as landmarker:
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

        height, width = frame.shape[:2]

        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        frame_timestamp_ms = int(time.time()*1000)

    # Our operations on the frame come here
    # Display the resulting frame
        
        face_landmarker_result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)
        lm = face_landmarker_result.face_landmarks[0][0]
        width = int(lm.x * width)
        height = int(lm.y * height)
        cv.circle(frame, (width, height), 4, (191, 95, 139), -1)

        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()