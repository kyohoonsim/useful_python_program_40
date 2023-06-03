import cv2
import numpy as np

MARGIN = 20

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
watermark = cv2.imread('watermark.png', cv2.IMREAD_COLOR)
watermark_background = np.zeros_like(img)
watermark_position = input("워터마크가 들어갈 위치 지정(LT:좌측 상단, LB:좌측 하단, C:정중앙, RT:우측 상단, RB:우측 하단>>")

if watermark_position == 'LT':
    watermark_background[MARGIN:watermark.shape[0]+MARGIN, MARGIN:watermark.shape[1]+MARGIN] = watermark
elif watermark_position == 'LB':
    watermark_background[watermark_background.shape[0]-watermark.shape[0]-MARGIN:watermark_background.shape[0]-MARGIN, MARGIN:watermark.shape[1]+MARGIN] = watermark
elif watermark_position == 'C':
    watermark_background[
        int(watermark_background.shape[0]/2)-int(watermark.shape[0]/2) : int(watermark_background.shape[0]/2)-int(watermark.shape[0]/2)+watermark.shape[0], 
        int(watermark_background.shape[1]/2)-int(watermark.shape[1]/2) : int(watermark_background.shape[1]/2)-int(watermark.shape[1]/2)+watermark.shape[1],
        ] = watermark
elif watermark_position == 'RT':
    watermark_background[MARGIN:watermark.shape[0]+MARGIN, watermark_background.shape[1]-watermark.shape[1]-MARGIN:watermark_background.shape[1]-MARGIN] = watermark
elif watermark_position == 'RB':
    watermark_background[watermark_background.shape[0]-watermark.shape[0]-MARGIN:watermark_background.shape[0]-MARGIN, watermark_background.shape[1]-watermark.shape[1]-MARGIN:watermark_background.shape[1]-MARGIN] = watermark

result_img = cv2.addWeighted(img, 1.0, watermark_background, 1.0, 0)
cv2.imwrite('test_result.png', result_img)
cv2.imshow('result', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()