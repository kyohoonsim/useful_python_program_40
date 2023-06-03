import os
import imghdr

path_dir = './src'
file_list = os.listdir(path_dir)
print(file_list)

img_file_list = []
for file in file_list:
    if imghdr.what(path_dir + '\\' + file):
        img_file_list.append(file)

print(img_file_list)