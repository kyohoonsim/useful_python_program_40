from random import choice
import time 
from functools import lru_cache

def make_menu(user_choice):
    print(f"{user_choice}을(를) 만듭니다.")
    time.sleep(1)
    return {
        "menu": user_choice,
        "price": 20000,
    }

@lru_cache(maxsize=2)
def get_menu(user_choice):
    return make_menu(user_choice)

if __name__ == "__main__":
    start = time.time()
    for i in range(10):
        user_choice = choice(["치킨", "피자", "떡볶이"])
        print(f'{i+1}번째 손님이 {user_choice}을(를) 주문합니다.')
        menu = get_menu(user_choice)
        print(f"주문하신 음식 여기 있습니다> {menu}\n")
    end = time.time()
    print(f"총 소요시간: {end-start: .3f} sec")