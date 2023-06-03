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

def get_cash_balance() -> int:
    PATH = "uapi/domestic-stock/v1/trading/inquire-psbl-order"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json", 
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC8908R", # 실전투자
        "custtype": "P", # 개인
    }
    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "PDNO": "005935", # 현금 잔고 조회 목적이므로 아무 종목번호를 입력해도 됨
        "ORD_UNPR": "50000", # 현금 잔고 조회 목적이므로 1주당 가격을 아무렇게나 입력해도 됨
        "ORD_DVSN": "01", # 시장가
        "CMA_EVLU_AMT_ICLD_YN": "Y", # CMA평가금액포함
        "OVRS_ICLD_YN": "Y" # 해외포함
    }
    res = requests.get(URL, headers=headers, params=params)
    cash_balance = int(res.json()['output']['ord_psbl_cash'])
    return cash_balance

ACCESS_TOKEN = get_access_token()
print(f"접근 토큰: {ACCESS_TOKEN}")

cash_balance = get_cash_balance()

print(f"현재 시간: {datetime.now()}")
print(f"현재 현금 잔고: {cash_balance}원")
