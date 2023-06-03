import schedule
import time
import datetime

my_money = 0

def earn_money():
    now = datetime.datetime.now()
    global my_money
    my_money += 100
    print(now, "잔고:", my_money)
    
schedule.every(1).seconds.do(earn_money)

while True:
    schedule.run_pending()
    time.sleep(1)