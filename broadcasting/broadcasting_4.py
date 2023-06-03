from gtts import gTTS
from playsound import playsound 
from datetime import datetime
import schedule
import time

text = '''
임직원 여러분 점심 시간입니다. 
오전 내내 일하시느라 고생하셨습니다. 
구내 식당에 맛있는 점심을 준비해놨으니 식사하러 이동하세요.
'''

tts = gTTS(text, lang='ko')
tts.save('result.mp3')

def broadcast():
    now = datetime.now()
    print(now, "방송 시작")
    playsound('result.mp3')

schedule.every().day.at("12:00").do(broadcast)

while True:
    schedule.run_pending()
    time.sleep(1)