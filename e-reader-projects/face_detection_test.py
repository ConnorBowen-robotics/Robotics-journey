import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

model_path = "/home/vooddoo/projects/robotics-journey/e-reader-projects/face_landmarker.task"

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE)

with FaceLandmarker.create_from_options(options) as landmarker:
    mp_image = mp.Image.create_from_file('/home/vooddoo/projects/robotics-journey/e-reader-projects/face.jpg')
    face_landmarker_result = landmarker.detect(mp_image)
    print(type(face_landmarker_result))
    print(dir(face_landmarker_result))
    print(face_landmarker_result.face_landmarks[0][0])