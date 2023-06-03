import requests
import argparse

parser = argparse.ArgumentParser(description="날씨고는 입력한 도시의 현재 기온을 알려주는 프로그램입니다.")
parser.add_argument('--city', required=True, help='현재 기온을 알고 싶은 도시명')
parser.add_argument('--num', required=False, default=1, help='조회 결과 수')
args = parser.parse_args()
city = args.city
num = args.num

url_front = "http://api.openweathermap.org/geo/1.0/direct?"
url_q = "q="
q = city
url_limit = "&limit=" + str(num)
url_appid = "&appid="
appid = "여러분이 발급받은 API 키"

url = url_front + url_q + q + url_limit + url_appid + appid

result = requests.get(url)
json_data = result.json()

print(f"날씨고에게 {q}의 현재 기온을 물어본 결과({len(json_data)}건)입니다")

url_front1 = "https://api.openweathermap.org/data/2.5/weather?"
url_lat = "lat="
url_lon = "&lon="
url_units = "&units=metric"

for i, data in enumerate(json_data, 1):
    x, y = data['lon'], data['lat']

    lat = str(y)
    lon = str(x)

    url1 = url_front1 + url_lat + lat + url_lon + lon + url_units + url_appid + appid

    result1 = requests.get(url1)
    json_data1 = result1.json()

    temperature = json_data1['main']['temp']
    name = json_data1['name']
    country = json_data1['sys']['country']
    print(f"{i}. 현재 {name} ({country}) 기온은 섭씨 {temperature}도입니다.")