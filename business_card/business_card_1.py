import cv2
import random
import numpy as np

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
width, height, colors = img.shape
print(width, height, colors)

if width > 1000 or height > 1000:
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) 
    width, height, colors = img.shape
    print(width, height, colors)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("test", img_gray)
cv2.waitKey(0)

img_thresh = cv2.adaptiveThreshold(img_gray, maxValue=255.0, 
                                adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                thresholdType=cv2.THRESH_BINARY_INV, blockSize=19, C=9)

cv2.imshow("test", img_thresh)
cv2.waitKey(0)

contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

img1 = img.copy()

for i in range(len(contours)):
    cv2.drawContours(img1, contours[i], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)

cv2.imshow("test", img1)
cv2.waitKey(0)

img2 = img.copy()
img_black = np.zeros((width, height, colors), dtype=np.uint8)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img2, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)
    cv2.rectangle(img_black, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)

cv2.imshow("test", img2)
cv2.waitKey(0) 

cv2.imshow("test", img_black)
cv2.waitKey(0) 