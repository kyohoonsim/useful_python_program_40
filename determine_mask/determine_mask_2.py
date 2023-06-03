import cv2
import cvlib as cv
import os
from datetime import datetime
from pytz import timezone

try:
    os.makedirs('./mask')
except FileExistsError:
    pass

webcam = cv2.VideoCapture(0)
 
if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    
sample_num = 0    
    
while webcam.isOpened():
    status, frame = webcam.read()
    sample_num += 1
    
    if not status:
        break
    
    if sample_num % 8  == 0:
        face, confidence = cv.detect_face(frame)
 
        for idx, f in enumerate(face):
            (startX, startY) = f[0], f[1]
            (endX, endY) = f[2], f[3]
            face_in_img = frame[startY:endY, startX:endX, :]
            
            now_time = datetime.now(timezone('Asia/Seoul')).strftime('%Y%m%d_%H%M%S%f')
            print(f'{now_time}에 얼굴 이미지 캡쳐')
            cv2.imwrite('./mask/face' + now_time + '.jpg', face_in_img)
 
    cv2.imshow("captured frames", frame)        
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()