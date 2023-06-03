import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

img = cv2.imread('nuddle.jpg', cv2.IMREAD_COLOR)
height, width, color = img.shape
print(width, height, color)

new_width = 400
new_height = int(height * new_width/width)
img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
img_cartoon = cv2.stylization(img_resized, sigma_s=150, sigma_r=0.25)
img_cartoon = cv2.ellipse(img_cartoon, (280, 80), (100, 60), 0, 0, 360, (230, 230, 230), -1)
print(type(img_cartoon))

img_pillow = Image.fromarray(img_cartoon)
print(type(img_pillow))

fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 24)
b,g,r,a = 0,0,0,255
draw = ImageDraw.Draw(img_pillow, 'RGBA')
draw.text((200, 70), "아니! 이 맛은!!!!", font=font, fill=(b,g,r,a))
img_numpy = np.array(img_pillow)
print(type(img_numpy))

cv2.imshow('test', img_numpy)
cv2.waitKey(0)