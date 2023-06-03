import time
import webbrowser
from datetime import datetime

start_date = datetime(2020, 8, 15) 
now = datetime.now() 
days_in_love = now - start_date 

message_list = ["안녕, 희야.\n", 
                "우리가 만난지 어느새 " + str(days_in_love.days) + "일이 되었네.\n", 
                "너를 만나고 난 후,\n", 
                "나는 완전히 다른 사람이 되었어..\n", 
                "앞으로 더 많은 행복을 함께 만들어가고 싶어.\n", 
                "우리 결혼하자!\n"] 

for message in message_list: 
    print(message) 
    time.sleep(3) 

while True: 
    answer = input("[선택] 프로포즈 수락은 Y, 거절은 N을 입력>>") 
    if answer in ['Y', 'y']: 
        url1 = 'https://www.youtube.com/watch?v=DgcBfR7Wjzw' 
        webbrowser.open(url1) 
        break 
    elif answer in ['N', 'n']: 
        url2 = 'https://www.youtube.com/watch?v=7hgJz4_SWbc' 
        webbrowser.open(url2) 
        break 
    else: 
        print('\n[경고] 제발 Y 또는 N을 입력해줘.... 그렇지 않으면 이 프로포즈는 끝나지 않아...\n') 