import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QWidget
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("각출 금액 랜덤 분할")
        self.setFixedWidth(600)

        self.amount = 0
        self.people = []
        self.btn_divide_amount_clicked_cnt = 0
                
        self.lb_amount = QLabel('금액 입력:')
        self.qle_amount = QLineEdit()
        self.lb_people = QLabel('게임 참여 멤버:')
        self.qle_people = QLineEdit()
        self.btn_submit = QPushButton('제출')
        self.btn_divide_amount = QPushButton('금액 분할')
        self.btn_matching_people = QPushButton('인원 매칭')
        self.qte_amount = QPlainTextEdit()
        self.qte_people = QPlainTextEdit()
        self.btn_reset = QPushButton('리셋')

        self.qle_amount.textChanged.connect(self.amount_changed)
        self.btn_submit.clicked.connect(self.btn_submit_clicked)
        self.btn_divide_amount.clicked.connect(self.btn_divide_amount_clicked)
        self.btn_matching_people.clicked.connect(self.btn_matching_people_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)

        self.btn_divide_amount.setEnabled(False)
        self.btn_matching_people.setEnabled(False)

        sub_layout1 = QHBoxLayout()
        sub_layout1.addWidget(self.qle_people)
        sub_layout1.addWidget(self.btn_submit)

        sub_layout2 = QHBoxLayout()
        sub_layout2.addWidget(self.btn_divide_amount)
        sub_layout2.addWidget(self.btn_matching_people)

        sub_layout3 = QHBoxLayout()
        sub_layout3.addWidget(self.qte_amount)
        sub_layout3.addWidget(self.qte_people)

        layout = QVBoxLayout()
        layout.addWidget(self.lb_amount)
        layout.addWidget(self.qle_amount)
        layout.addWidget(self.lb_people)
        layout.addLayout(sub_layout1)
        layout.addLayout(sub_layout2)
        layout.addLayout(sub_layout3)
        layout.addWidget(self.btn_reset)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def amount_changed(self, amount):
        print(amount)
        self.amount = amount

    def btn_submit_clicked(self):
        self.people_str = self.qle_people.text()
        self.people = self.people_str.split(',')
        print(self.people)
        self.btn_divide_amount.setEnabled(True)

    def btn_divide_amount_clicked(self):
        self.btn_divide_amount_clicked_cnt += 1
        self.amount = int(self.amount)

        if self.btn_divide_amount_clicked_cnt < len(self.people):
            temp = random.randint(0, self.amount)
            self.amount -= temp
            self.qte_amount.appendPlainText(str(temp))
        elif self.btn_divide_amount_clicked_cnt == len(self.people):
            self.qte_amount.appendPlainText(str(self.amount))
            self.btn_matching_people.setEnabled(True)

    def btn_matching_people_clicked(self):
        if len(self.people) > 0:
            random.shuffle(self.people)
            temp = self.people.pop()
            self.qte_people.appendPlainText(str(temp))

    def btn_reset_clicked(self):
        self.amount = 0
        self.people = []
        self.btn_divide_amount_clicked_cnt = 0

        self.qle_amount.clear()
        self.qle_people.clear()
        self.qte_amount.clear()
        self.qte_people.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()