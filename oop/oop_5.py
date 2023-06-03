class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"저는 {self.name}입니다.")


class Developer(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def coding(self):
        print(f"{self.name}은 {self.language}으로 코딩을 합니다.")


class Singer(Person):
    def __init__(self, name, representative_song):
        super().__init__(name)
        self.representative_song = representative_song

    def sing(self):
        print(f"{self.name}은 노래를 합니다.")

    def show_representative_song(self):
        print(f"{self.name}의 대표곡은 {self.representative_song}입니다.")


class SoccerPlayer(Person):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def play_soccer(self):
        print(f"{self.name}은 축구를 합니다.")

    def show_team(self):
        print(f"{self.name}은 {self.team} 소속입니다.")


p1 = Developer('심교훈', '파이썬')
p2 = Developer('빌게이츠', 'C언어')
p3 = Singer('아이유', '좋은날')
p4 = Singer('BTS', 'Dynamite')
p5 = SoccerPlayer('손흥민', '토트넘핫스퍼')
p6 = SoccerPlayer('황희찬', '울버햄튼')

p1.introduce()
p1.coding()

p2.introduce()
p2.coding()

p3.introduce()
p3.sing()
p3.show_representative_song()

p4.introduce()
p4.sing()
p4.show_representative_song()

p5.introduce()
p5.play_soccer()
p5.show_team()

p6.introduce()
p6.play_soccer()
p6.show_team()