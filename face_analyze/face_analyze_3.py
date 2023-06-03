from deepface import DeepFace
import cv2
import numpy as np

face_analysis = DeepFace.analyze(img_path = "test1.jpg")
print(face_analysis)

img = cv2.imread("test1.jpg", cv2.IMREAD_COLOR)

region = face_analysis[0]['region']
pt1 = region['x'], region['y']
pt2 = region['x'] + region['w'], region['y'] + region['h']
face = img[pt1[1]:pt2[1], pt1[0]:pt2[0]]

img = img.astype('int32')
img = np.clip(img - 50, 0, 255)
img = img.astype('uint8')

img[pt1[1]:pt2[1], pt1[0]:pt2[0]] = face

cv2.rectangle(img, pt1=pt1, pt2=pt2, color=(241, 242, 64), thickness=1)
cv2.imshow("CIA", img)
cv2.waitKey(0)