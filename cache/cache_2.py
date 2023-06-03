import time  

def time_check(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} 함수 실행에 {end-start:.2f}초 소요되었습니다.")
    return wrapper

@time_check
def test():
    print("test 함수 시작")
    time.sleep(5)
    print("test 함수 끝")

@time_check
def another_test():
    print("another_test 함수 시작")
    time.sleep(7)
    print("another_test 함수 끝")

test()
another_test()