import random

numbers = list(range(1, 46))
print(numbers)

selected_numbers = random.sample(numbers, 6)
print(selected_numbers)

selected_numbers.sort()
print(selected_numbers)