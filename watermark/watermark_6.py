import cv2
import numpy as np
import os
import imghdr
import argparse

MARGIN = 20

parser = argparse.ArgumentParser(description="src 폴더 안에 있는 이미지들에 대해 워터마크 처리를 해주는 프로그램입니다. 워터마킹 처리를 해줄 이미지들을 src 폴더에 모두 넣어주세요.")
parser.add_argument('--watermark', required=True, help='워터마크 이미지 파일명')
parser.add_argument('--position', required=True, help="워터마크가 들어갈 위치(LT:좌측 상단, LB:좌측 하단, C:정중앙, RT:우측 상단, RB:우측 하단)")
args = parser.parse_args()
watermark_position = args.position
watermark_img = args.watermark

path_dir = './src'
file_list = os.listdir(path_dir)

try:
    os.makedirs('result')
except FileExistsError:
    pass

img_file_list = []
for file in file_list:
    if imghdr.what(path_dir + '\\' + file):
        img_file_list.append(file)

for file in img_file_list:
    img = cv2.imread(path_dir + '\\' + file, cv2.IMREAD_COLOR)
    watermark = cv2.imread(watermark_img, cv2.IMREAD_COLOR)
    watermark_background = np.zeros_like(img)

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
    else:
        print("워터마크 위치 지정에 관하여 잘못 입력하셨습니다.")
        break

    result_img = cv2.addWeighted(img, 1.0, watermark_background, 1.0, 0)
    cv2.imwrite('./result/result_' + file, result_img)