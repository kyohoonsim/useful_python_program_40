import requests

url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = "q="
q = "Seoul"
url_limit = "&limit=1"
url_appid = "&appid="
appid = "여러분이 발급받은 API 키"

url = url_front + url_q + q + url_limit + url_appid + appid
print(url, "\n")

result = requests.get(url)
json_data = result.json()
print(json_data, "\n")

x, y = json_data[0]['lon'], json_data[0]['lat']
print(f"{q}의 위도(y), 경도(x) 좌표: ({y}, {x})")

url_front1 = "https://api.openweathermap.org/data/2.5/weather?"
url_lat = "lat="
lat = str(y)
url_lon = "&lon="
lon = str(x)
url_units = "&units=metric"

url1 = url_front1 + url_lat + lat + url_lon + lon + url_units + url_appid + appid
print(url1, "\n")

result1 = requests.get(url1)
json_data1 = result1.json()
print(json_data1, "\n")

temperature = json_data1['main']['temp']
print(f"현재 {q} 기온은 섭씨 {temperature}도입니다.")