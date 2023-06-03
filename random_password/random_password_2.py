import string
import random
 
new_pw = ""

for i in range(5):
    new_pw += random.choice(string.ascii_letters)

for i in range(3):
    new_pw += random.choice(string.digits)

for i in range(2):
    new_pw += random.choice("!@#$%^&*")
 
print("생성된 랜덤 비밀번호", new_pw)

new_pw_shuffle = "".join(random.sample(new_pw, len(new_pw)))
print("생성된 랜덤 비밀번호(섞은 후)", new_pw_shuffle)