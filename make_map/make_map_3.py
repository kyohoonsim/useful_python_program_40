import requests
import pandas as pd

apiurl = "http://api.vworld.kr/req/address?"
params = {
    "service": "address",
    "request": "getcoord",
    "crs": "epsg:4326",
    "format": "json",
    "type": "road",
    "key": "여러분이 발급받은 인증키"
}

df = pd.read_excel('제천맛집리스트.xlsx')
print(df)

for idx, row in df.iterrows():
    address = row['주소(도로명)']
    params['address'] = address

    response = requests.get(apiurl, params=params)

    if response.status_code == 200:
        json_data = response.json()

        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        print(f"주소: {address}, 위도: {y}, 경도: {x}")