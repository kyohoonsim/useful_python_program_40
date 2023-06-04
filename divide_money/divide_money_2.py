import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("갹출 금액 랜덤 분할")
        self.setFixedWidth(600)
        
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()