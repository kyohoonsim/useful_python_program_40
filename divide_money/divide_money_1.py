import random

remaining_amount = 85000
people = 5

money_per_person = []
for i in range(people-1):
    temp = random.randint(0, remaining_amount)
    remaining_amount -= temp
    money_per_person.append(temp)

money_per_person.append(remaining_amount)

print("각 사람이 지불해야할 금액:", money_per_person)
print("총합: ", sum(money_per_person))

money_per_person.sort(reverse=True)
print("각 사람이 지불해야할 금액(내림차순):", money_per_person)