from datetime import datetime
import time
from trading_funcs import get_current_price, get_stock_balance, get_cash_balance, buy_stock, sell_stock 

while True:
    try:
        print(f"\n\n[나만의주식매매프로그램 v0.1]")
        print(f"******* 메뉴 *******")
        print(f"1. 현재 주가 확인")
        print(f"2. 주식 잔고 조회")
        print(f"3. 현금 잔고 조회")
        print(f"4. 주식 매수")
        print(f"5. 주식 매도")
        print(f"0. 프로그램 종료")
        print(f"********************")

        choice = int(input("원하는 작업을 선택하세요> "))

        if choice == 0:
            print(f"\n[프로그램 종료]")
            break
        elif choice == 1:
            print(f"\n[주가 확인]")
            code = input("종목 코드를 입력하세요> ")
            current_price = get_current_price(code)
            print(f"현재 시간: {datetime.now()}")
            print(f"현재 주가: {current_price}원")
        elif choice == 2:
            print(f"\n[주식 잔고 조회]")
            print(f"현재 시간: {datetime.now()}")
            get_stock_balance()
        elif choice == 3:
            print(f"\n[현금 잔고 조회]")
            cash_balance = get_cash_balance()
            print(f"현재 시간: {datetime.now()}")
            print(f"현재 현금 잔고: {cash_balance}원")
        elif choice == 4:
            print(f"\n[주식 매수]")
            code = input("종목 코드를 입력하세요> ")
            qty = int(input("매수 수량을 입력하세요> "))
            print(f"현재 시간: {datetime.now()}")
            buy_stock(code, qty)
        elif choice == 5:
            print(f"\n[주식 매도]")
            code = input("종목 코드를 입력하세요> ")
            qty = int(input("매도 수량을 입력하세요> "))
            print(f"현재 시간: {datetime.now()}")
            sell_stock(code, qty)

        time.sleep(3)
    except:
        pass