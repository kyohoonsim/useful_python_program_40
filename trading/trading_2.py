import yaml
import requests 
import json
from datetime import datetime
import time

with open('config.yaml') as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)

APP_KEY = cfg['APP_KEY']
APP_SECRET = cfg['APP_SECRET']
CANO = cfg['CANO']
ACNT_PRDT_CD = cfg['ACNT_PRDT_CD']
URL_BASE = cfg['URL_BASE']

def get_access_token(): 
    PATH = "oauth2/tokenP"
    URL = f"{URL_BASE}/{PATH}"
    headers = {"content-type": "application/json"}
    body = {
        "grant_type": "client_credentials",
        "appkey": APP_KEY, 
        "appsecret": APP_SECRET
    }
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    ACCESS_TOKEN = res.json()["access_token"]
    return ACCESS_TOKEN

def get_current_price(code: str) -> int:
    PATH = "uapi/domestic-stock/v1/quotations/inquire-price"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json", 
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "FHKST01010100" # 주식 현재가 시세
    }
    params = {
        "fid_cond_mrkt_div_code": "J", # 주식, ETF, ETN
        "fid_input_iscd": code,
    }
    res = requests.get(URL, headers=headers, params=params)
    current_price = int(res.json()['output']['stck_prpr'])
    return current_price

ACCESS_TOKEN = get_access_token()
print(f"접근 토큰: {ACCESS_TOKEN}")

stock_code = '005935'

while True:
    current_price = get_current_price(stock_code)
    print(f"현재 시간: {datetime.now()}")
    print(f"현재 주가: {current_price}원")

    time.sleep(2)