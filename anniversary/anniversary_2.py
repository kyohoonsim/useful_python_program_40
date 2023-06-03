from datetime import datetime

now = datetime.now()
wedding_day = datetime(2017, 7, 22)
roa_birth = datetime(2018, 5, 7)
ina_birth = datetime(2019, 7, 27)

wedding_days = now - wedding_day
roa_days = now - roa_birth
ina_days = now - ina_birth

print(f"우리 결혼한지 +{wedding_days.days}일째")
print(f"로아 태어난지 +{roa_days.days}일째")
print(f"인아 태어난지 +{ina_days.days}일째")