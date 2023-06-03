import schedule
import time
import datetime

users = [
    ('김개똥', 19),
    ('이말똥', 2),
    ('박새똥', 29),
    ('최소똥', 19),
    ('김닭똥', 7),
]

def pay():
    for user in users:
        now = datetime.datetime.now()

        if now.day == user[1]:
            print(user[0] + "님, 결제 실시", now)
    
schedule.every().day.at('00:00').do(pay)

while True:
    schedule.run_pending()
    time.sleep(1)