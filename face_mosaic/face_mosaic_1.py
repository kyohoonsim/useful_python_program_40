import cvlib
import cv2

img = cv2.imread('test.jpg')

faces, confidence = cvlib.detect_face(img)

for face in faces:
    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]

    cv2.rectangle(img, (startX,startY), (endX,endY), (0,255,0), 2)

cv2.imshow("detect faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()