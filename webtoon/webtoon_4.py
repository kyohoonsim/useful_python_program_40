import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

new_width = 400
fontpath = "fonts/gulim.ttc"
font = ImageFont.truetype(fontpath, 20)
b,g,r,a = 0,0,0,255

script = ["화창한 주말 아침", "타요, 오늘 주말인데\n우리 뭐하고 놀까?", "아빠~~~ 우리 같이\n나가서 놀아요~~~"]
ellipse_center = [(0, 0), (200, 240), (180, 230)]
text_start = [(150, 70), (110, 220), (90, 210)]

result_img = np.zeros((0, 400, 3), np.uint8)

for i in range(1, 4):
    img = cv2.imread('cut' + str(i) + '.jpg', cv2.IMREAD_COLOR)
    height, width, color = img.shape
    new_height = int(height * new_width/width)
    img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    img_cartoon = cv2.stylization(img_resized, sigma_s=150, sigma_r=0.25)
    
    if i != 1:
        img_cartoon = cv2.ellipse(img_cartoon, ellipse_center[i-1], (100, 60), 0, 0, 360, (230, 230, 230), -1)
    
    img_pillow = Image.fromarray(img_cartoon)
    draw = ImageDraw.Draw(img_pillow, 'RGBA')
    draw.text(text_start[i-1], script[i-1], font=font, fill=(b,g,r,a))
    img_numpy = np.array(img_pillow)

    result_img = cv2.vconcat([result_img, img_numpy])

cv2.imshow('test', result_img)
cv2.waitKey(0)
cv2.imwrite("3cut_webtoon.jpg", result_img)