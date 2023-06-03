class Developer:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"저는 {self.name}입니다.")

    def coding(self):
        print(f"{self.name}은 코딩을 합니다.")


class Singer:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"저는 {self.name}입니다.")

    def sing(self):
        print(f"{self.name}은 노래를 합니다.")


class SoccerPlayer:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"저는 {self.name}입니다.")

    def play_soccer(self):
        print(f"{self.name}은 축구를 합니다.")


p1 = Developer('심교훈')
p2 = Developer('빌게이츠')
p3 = Singer('아이유')
p4 = Singer('BTS')
p5 = SoccerPlayer('손흥민')
p6 = SoccerPlayer('황희찬')

p1.introduce()
p1.coding()
p2.introduce()
p2.coding()
p3.introduce()
p3.sing()
p4.introduce()
p4.sing()
p5.introduce()
p5.play_soccer()
p6.introduce()
p6.play_soccer()