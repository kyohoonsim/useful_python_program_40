import schedule
import time
import datetime

def drink_water():
    now = datetime.datetime.now()
    print(now, "주인님, 물 마실 시간입니다.")
    
schedule.every(2).hours.do(drink_water)

while True:
    schedule.run_pending()
    time.sleep(1)