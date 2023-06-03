import cv2

img = cv2.imread('nuddle.jpg', cv2.IMREAD_COLOR)
height, width, color = img.shape
print(width, height, color)

new_width = 400
new_height = int(height*new_width/width)
img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
img_cartoon = cv2.stylization(img_resized, sigma_s=150, sigma_r=0.25)

cv2.imshow('test', img_cartoon)
cv2.waitKey(0)