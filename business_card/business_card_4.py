import cv2
import random
import numpy as np
import math

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
img_black1 = img_black.copy()

candidates = []

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    
    if w >= width/2 or h >= height/2:
        cv2.rectangle(img_black, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)
        
        if (1 < w/h < 2) or (1 < h/w < 2):
            cv2.rectangle(img_black1, pt1=(x,y), pt2=(x+w, y+h), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)
            candidates.append({'contour':contour, 'x':x, 'y':y, 'w':w, 'h':h})

cv2.imshow("test", img_black)
cv2.waitKey(0)  

cv2.imshow("test", img_black1)
cv2.waitKey(0)  

area_list = []

if len(candidates) >= 2:
    for candidate in candidates:
        area = candidate['w'] * candidate['h']
        area_list.append(area)

    min_area = min(area_list)
    min_index = area_list.index(min_area)
    print(min_area, min_index)

else:
    min_index = 0

bussiness_card = candidates[min_index]

img3 = img.copy()

cv2.rectangle(img3, pt1=(bussiness_card['x'], bussiness_card['y']), 
            pt2=(bussiness_card['x']+bussiness_card['w'], bussiness_card['y']+bussiness_card['h']), 
            color=(0, 0, 255), thickness=2)
cv2.drawContours(img, bussiness_card['contour'], -1, (255, 0, 0), 2)

cv2.imshow("test", img3)
cv2.waitKey(0) 

cv2.imshow("test", img)
cv2.waitKey(0) 

x_min = width
x_max = 0
y_min = height
y_max = 0

for point in bussiness_card['contour']:
    if point[0][0] < x_min:
        x_min = point[0][0]
        x_min_partner = point[0][1]
    
    if point[0][0] > x_max:
        x_max = point[0][0]
        x_max_partner = point[0][1]

    if point[0][1] < y_min:
        y_min = point[0][1]
        y_min_partner = point[0][0]
    
    if point[0][1] > y_max:
        y_max = point[0][1]
        y_max_partner = point[0][0]

pt1 = (x_min, x_min_partner)
pt2 = (y_min_partner, y_min)
pt3 = (y_max_partner, y_max)
pt4 = (x_max, x_max_partner)

print(pt1, pt2, pt3, pt4)

cv2.circle(img, pt1, radius=5, color=(0, 0, 255), thickness=-1)
cv2.circle(img, pt2, radius=5, color=(0, 0, 255), thickness=-1)
cv2.circle(img, pt3, radius=5, color=(0, 0, 255), thickness=-1)
cv2.circle(img, pt4, radius=5, color=(0, 0, 255), thickness=-1)

cv2.imshow("test", img)
cv2.waitKey(0)

new_width = int((math.dist(pt1, pt2) + math.dist(pt3, pt4))/2)
new_height = int((math.dist(pt2, pt4) + math.dist(pt1, pt3))/2)

src = np.float32([list(pt1), list(pt2), list(pt3), list(pt4)])
dst = np.float32([[0, 0], [new_width, 0], [0, new_height], [new_width, new_height]])

mat = cv2.getPerspectiveTransform(src, dst)

img_card = cv2.warpPerspective(img, mat, (new_width, new_height))

if new_width < new_height:
    img_card = cv2.rotate(img_card, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("test", img_card)
cv2.waitKey(0)

cv2.imwrite("bussiness_card.jpg", img_card)