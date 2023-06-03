from itertools import starmap
import sys
import re

user_input = input(
'''[Hex 코드 또는 RGB 색상을 입력해주세요]
- Hex 코드 입력 예시: #123456
- RGB 색상 입력 예시: 18 52 86 
>> ''')

if user_input[0] == '#':
    if len(user_input) == 7:

        for i in user_input[1:]:
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
                sys.exit('\n[에러] Hex 코드 입력시에는 0에서 F(f) 이외의 문자/숫자가 포함되어서는 안됩니다.')
        
        rgb = [(user_input[1:3], 16), (user_input[3:5], 16), (user_input[5:], 16)]
        rgb_list = list(starmap(int, rgb))
        rgb_tuple = tuple(rgb_list)
        print("\n[변환 결과] ", user_input, ' => ', rgb_tuple)
    else:
        sys.exit('\n[에러] Hex 코드 입력시에는 # 제외 6자리의 hex 코드를 입력해야 합니다.')
else:
    rgb_str_list = re.findall(r'\d+', user_input)
    rgb_tuple = tuple(map(int, rgb_str_list))

    if len(rgb_tuple) != 3:
        sys.exit('\n[에러] RGB 색상 입력시에는 숫자 세 개를 입력해야 합니다.')    

    hex_code = '#'

    for i in rgb_tuple:
        if i >= 0 and i <= 255:
            temp = hex(i)[2:]

            if len(temp) == 1:
                temp = '0' + temp

            hex_code += temp.upper()
        else:
            sys.exit('\n[에러] RGB 색상 입력시에는 0~255 값을 입력해야 합니다.')

    print("\n[변환 결과] ", rgb_tuple, ' => ', hex_code)