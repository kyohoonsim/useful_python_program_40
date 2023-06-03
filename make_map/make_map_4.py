import folium
import requests
import pandas as pd

jecheon_map = folium.Map(location=[37.14315, 128.2016], zoom_start=13)

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

for idx, row in df.iterrows():
    address = row['주소(도로명)']
    params['address'] = address

    response = requests.get(apiurl, params=params)

    if response.status_code == 200:
        json_data = response.json()

        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']

        folium.Marker([y, x], popup=row['이름']).add_to(jecheon_map)

jecheon_map.save('jecheon_map.html')