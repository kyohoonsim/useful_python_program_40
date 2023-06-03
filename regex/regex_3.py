import re

with open("regex_test2.txt", "r") as File:
    data = File.read()

print(data)

p1 = re.compile(r"\d{6}[-]\d{7}")
rrn_list = re.findall(p1, data)
print(rrn_list)

p2 = re.compile(r"\d{2,3}[-]\d{4}[-]\d{4}")
phone_list = re.findall(p2, data)
print(phone_list)
