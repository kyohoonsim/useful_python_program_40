import random

numbers = list(range(1, 46))

for i in range(1, 6):
    selected_numbers = random.sample(numbers, 6)
    selected_numbers.sort()
    print(str(i) + "게임: ", selected_numbers)