import yaml
import requests 
import json
from datetime import datetime

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

def hash_key(body):
    PATH = "uapi/hashkey"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        'content-Type': 'application/json',
        'appKey': APP_KEY,
        'appSecret': APP_SECRET,
    }
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    hashkey = res.json()["HASH"]
    return hashkey

def sell_stock(code: str, qty: int):
    PATH = "uapi/domestic-stock/v1/trading/order-cash"
    URL = f"{URL_BASE}/{PATH}"
    body = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": code,
        "ORD_DVSN": "01", # 시장가
        "ORD_QTY": str(qty),
        "ORD_UNPR": "0",
    }
    headers = {
        "Content-Type":"application/json", 
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC0801U", # 주식 현금 매도 주문
        "custtype": "P", # 개인
        "hashkey": hash_key(body)
    }
    res = requests.post(URL, headers=headers, data=json.dumps(body))

    success = res.json()['rt_cd']
    print(f"{res.json()['msg1']}")

    if success == '0':
        print(f"종목 코드 {code} {qty}주 매도에 성공하셨습니다.")
    else:
        print(f"종목 코드 {code} {qty}주 매도에 실패하셨습니다.")

ACCESS_TOKEN = get_access_token()
print(f"접근 토큰: {ACCESS_TOKEN}")

stock_code = '005935'
qty = 1

print(f"현재 시간: {datetime.now()}")
sell_stock(stock_code, qty)
