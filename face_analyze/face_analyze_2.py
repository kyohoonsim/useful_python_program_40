from deepface import DeepFace
import cv2

face_analysis = DeepFace.analyze(img_path = "test1.jpg")
print(face_analysis)

img = cv2.imread("test1.jpg", cv2.IMREAD_COLOR)

region = face_analysis[0]['region']
pt1 = region['x'], region['y']
pt2 = region['x'] + region['w'], region['y'] + region['h']

cv2.rectangle(img, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)
cv2.imshow("CIA", img)
cv2.waitKey(0)