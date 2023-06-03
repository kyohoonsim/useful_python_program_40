import cvlib
import cv2

N = 2

img = cv2.imread('test1.jpg')

faces, confidence = cvlib.detect_face(img)
faces_area = []

for face in faces:
    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]

    face_area = (endX - startX)*(endY - startY)
    faces_area.append(face_area)

print(faces_area)

faces_area_sorted = sorted(faces_area, reverse=True)
print(faces_area_sorted)

min_face_area = min(faces_area_sorted[0:N])
print("모자이크 처리 기준이 될 얼굴 사이즈: ", min_face_area)

for face in faces:
    (startX,startY) = face[0],face[1]
    (endX,endY) = face[2],face[3]

    face_area = (endX - startX)*(endY - startY)

    if face_area < min_face_area:
        face_region = img[startY:endY, startX:endX]
        
        M, N, D = face_region.shape

        face_region = cv2.resize(face_region, None, fx=0.05, fy=0.05, interpolation=cv2.INTER_AREA)
        face_region = cv2.resize(face_region, (N, M), interpolation=cv2.INTER_AREA)
        img[startY:endY, startX:endX] = face_region

cv2.imshow("detect and mosaic stranger faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test1_result.jpg', img) 