import requests

apiurl = "http://api.vworld.kr/req/address?"
params = {
    "service": "address",
    "request": "getcoord",
    "crs": "epsg:4326",
    "address": "충북 제천시 의병대로 165",
    "format": "json",
    "type": "road",
    "key": "여러분이 발급받은 인증키"
}

response = requests.get(apiurl, params=params)

if response.status_code == 200:
    json_data = response.json()
    print(json_data)

    x = json_data['response']['result']['point']['x']
    y = json_data['response']['result']['point']['y']
    print(f"위도: {y}, 경도: {x}")