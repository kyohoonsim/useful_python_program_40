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

gender = face_analysis[0]['dominant_gender']
age = str(face_analysis[0]['age'])
race = face_analysis[0]['dominant_race']
emotion = face_analysis[0]['dominant_emotion']
race_per = str(round(face_analysis[0]['race'][race], 1))
emotion_per = str(round(face_analysis[0]['emotion'][emotion], 1) )

cv2.putText(img, 'Gender: ' + gender, (pt2[0]+10, pt1[1]+10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)
cv2.putText(img, 'Age: ' + age, (pt2[0]+10, pt1[1]+30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)
cv2.putText(img, 'Race: ' + race + ' ' + race_per + '%', (pt2[0]+10, pt1[1]+50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)
cv2.putText(img, 'Emotion: ' + emotion + ' ' + emotion_per + '%', (pt2[0]+10, pt1[1]+70), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (241, 242, 64), 1, cv2.LINE_AA)

cv2.imshow("CIA", img)
cv2.waitKey(0)