import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model('model.h5')

img = cv2.imread('test1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("test", img)
cv2.waitKey(0)

img1 = img.copy()
_, img1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

img2 = img.copy()

for i in range(len(contours)):
    cv2.drawContours(img2, contours[i], -1, (255,0,0), 2)

cv2.imshow("test", img2)
cv2.waitKey(0)

img3 = img.copy()
num_candidates = []

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    num_candidates.append((x,y,w,h))
    cv2.rectangle(img3, pt1=(x,y), pt2=(x+w, y+h), color=(255,0,0), thickness=1)

cv2.imshow("test", img3)
cv2.waitKey(0) 

num_candidates = sorted(num_candidates)
num_candidates1 = []

for candidate in num_candidates:
    w,h = candidate[2],candidate[3]
    if h/w > 0.5 and w > 3 and h > 3:
        num_candidates1.append(candidate)

phone_num = []

if len(num_candidates1) == 11:
    for candidate in num_candidates1:
        x,y,w,h = candidate[0],candidate[1],candidate[2],candidate[3]
        img_num = img[y:y+h, x:x+w]
       
        _, img_num = cv2.threshold(img_num, 127, 255, cv2.THRESH_BINARY_INV)
        margin = int(max(w, h)/4)
        img_black = np.zeros((h+2*margin, w+2*margin), dtype=np.uint8)
        img_black[margin:margin+h, margin:margin+w] = img_num
        img_black = cv2.resize(img_black, (28, 28), interpolation=cv2.INTER_AREA)

        cv2.imshow("test", img_black)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        x = img_to_array(img_black)/255.0
        x = np.expand_dims(x[:,:,0], axis=0)

        prediction = model.predict(x)
        phone_num.append(np.argmax(prediction))
else:
    raise Exception("전화번호 11자리를 제대로 찾아내지 못했습니다.")

print(phone_num)

phone_num_str = [str(num) for num in phone_num]
print(f"검출된 전화번호: {''.join(phone_num_str)}")
