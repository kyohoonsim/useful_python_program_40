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

def get_stock_balance():
    PATH = "uapi/domestic-stock/v1/trading/inquire-balance"
    URL = f"{URL_BASE}/{PATH}"
    headers = {
        "Content-Type": "application/json", 
        "authorization": f"Bearer {ACCESS_TOKEN}",
        "appKey": APP_KEY,
        "appSecret": APP_SECRET,
        "tr_id": "TTTC8434R", # 실전투자 - 주식 잔고 조회
        "custtype": "P", # 개인
    }
    params = {
        "CANO": CANO,
        "ACNT_PRDT_CD": ACNT_PRDT_CD,
        "AFHR_FLPR_YN": "N",
        "OFL_YN": "",
        "INQR_DVSN": "02", # 조회구분 - 종목별
        "UNPR_DVSN": "01",
        "FUND_STTL_ICLD_YN": "N", # 펀드결제분포함여부 - 포함하지 않음
        "FNCG_AMT_AUTO_RDPT_YN": "N",
        "PRCS_DVSN": "00", # 처리구분 - 전일매매미포함
        "CTX_AREA_FK100": "",
        "CTX_AREA_NK100": "",
    }
    res = requests.get(URL, headers=headers, params=params)
    stock_list = res.json()['output1']

    for i, stock in enumerate(stock_list, 1):
        print(f"{i}. {stock['prdt_name']}({stock['pdno']})")
        print(f"\t보유수량: {stock['hldg_qty']}주")
        print(f"\t평가금액: {stock['evlu_amt']}원")
        print(f"\t매입금액: {stock['pchs_amt']}원")
        print(f"\t평가손익금액: {stock['evlu_pfls_amt']}원\n")

ACCESS_TOKEN = get_access_token()
print(f"접근 토큰: {ACCESS_TOKEN}")

print(f"현재 시간: {datetime.now()}")
get_stock_balance()
