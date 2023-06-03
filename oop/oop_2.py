class Person:
    def __init__(self, name, job, sex):
        self.name = name
        self.job = job
        self.sex = sex

    def introduce(self):
        print(f"{self.name}의 직업은 {self.job}이고 성별은 {self.sex}입니다.")    


p1 = Person('심교훈', '개발자', '남자')
p1.introduce()

p2 = Person('아이유', '가수', '여자')
p2.introduce()

p3 = Person('손흥민', '축구선수', '남자')
p3.introduce()