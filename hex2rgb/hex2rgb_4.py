from itertools import starmap

user_input = input(
'''[Hex 코드 또는 RGB 색상을 입력해주세요]
- Hex 코드 입력 예시: #123456
- RGB 색상 입력 예시: 18 52 86 
>> ''')

if user_input[0] == '#':
    rgb = [(user_input[1:3], 16), (user_input[3:5], 16), (user_input[5:], 16)]
    rgb_list = list(starmap(int, rgb))
    rgb_tuple = tuple(rgb_list)
    print("\n[변환 결과] ", user_input, ' => ', rgb_tuple)
else:
    rgb = user_input.split(" ")
    rgb_tuple = tuple(map(int, rgb))

    hex_code = '#'

    for i in rgb_tuple:
        temp = hex(i)[2:]

        if len(temp) == 1:
            temp = '0' + temp

        hex_code += temp.upper()

    print("\n[변환 결과] ", rgb_tuple, ' => ', hex_code)