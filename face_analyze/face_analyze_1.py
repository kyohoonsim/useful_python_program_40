from deepface import DeepFace

face_analysis = DeepFace.analyze(img_path = "test.jpg")
print(face_analysis)