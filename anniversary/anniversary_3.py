from datetime import datetime, timedelta

plus_days = 2000
wedding_day = datetime(2017, 7, 22)
the_day = wedding_day + timedelta(days=plus_days) 
print(f"우리 결혼한지 +{plus_days}일은 {the_day.year}년 {the_day.month}월 {the_day.day}일")
