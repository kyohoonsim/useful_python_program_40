rgb = (255, 238, 221)

hex_code = '#'

for i in rgb:
    temp = hex(i)[2:]

    if len(temp) == 1:
        temp = '0' + temp
        
    hex_code += temp.upper()

print(rgb, ' => ', hex_code)