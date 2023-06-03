import cvlib
import cv2

img = cv2.imread('test.jpg')

faces, confidence = cvlib.detect_face(img)

for face in faces:
    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]

    face_region = img[startY:endY, startX:endX]
    M, N, D = face_region.shape

    face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
    face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
    img[startY:endY, startX:endX] = face_region

cv2.imshow("detect and mosaic faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test_result.jpg', img)  