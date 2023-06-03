from itertools import starmap

hex_code = '#FFEEDD'

rgb = [(hex_code[1:3], 16), (hex_code[3:5], 16), (hex_code[5:], 16)]
rgb_list = list(starmap(int, rgb))
print(rgb_list)

rgb_tuple = tuple(rgb_list)
print(rgb_tuple)

print(hex_code, ' => ', rgb_tuple)