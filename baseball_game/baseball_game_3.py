import random

numbers = list(range(0, 10))
three_numbers = random.sample(numbers, 3)
print("맞춰야할 숫자:", three_numbers)

round = 1

while True:
    strike = 0
    ball = 0

    print("\n[" + str(round) + "라운드]\n")

    num1, num2, num3 = map(int, input("0-9 사이의 숫자 세 개 입력(중복 안됨). ex)3 6 9 >>").split())

    if three_numbers[0] == num1:
        strike += 1
    if three_numbers[1] == num2:
        strike += 1
    if three_numbers[2] == num3:
        strike += 1

    if three_numbers[1] == num1 or three_numbers[2] == num1:
        ball += 1
    if three_numbers[0] == num2 or three_numbers[2] == num2:
        ball += 1
    if three_numbers[0] == num3 or three_numbers[1] == num3:
        ball += 1

    print(strike, "strike", ball, "ball\n")

    if strike == 3:
        print("[게임 끝]", round, "라운드만에 맞추셨습니다.")
        break

    round += 1

