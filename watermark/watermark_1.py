import cv2
import numpy as np

img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
watermark = cv2.imread('watermark.png', cv2.IMREAD_COLOR)

watermark_background = np.zeros_like(img)
watermark_background[0:watermark.shape[0], 0:watermark.shape[1]] = watermark
cv2.imshow('background', watermark_background)

result_img = cv2.addWeighted(img, 1.0, watermark_background, 1.0, 0)
cv2.imwrite('test_result.png', result_img)
cv2.imshow('result', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()