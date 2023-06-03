import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("아기 재우기")
    self.setFixedSize(QSize(600, 400))
    self.audio1_btn = QPushButton('백색소음')
    self.audio2_btn = QPushButton('계곡물소리')
    self.audio3_btn = QPushButton('빗소리')

    self.audio1_btn.clicked.connect(self.audio1_btn_clicked)
    self.audio2_btn.clicked.connect(self.audio2_btn_clicked)
    self.audio3_btn.clicked.connect(self.audio3_btn_clicked)

    layout = QHBoxLayout()
    layout.addWidget(self.audio1_btn)
    layout.addWidget(self.audio2_btn)
    layout.addWidget(self.audio3_btn)

    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

  def audio1_btn_clicked(self):
    print("백색소음 버튼이 클릭되었습니다!")

  def audio2_btn_clicked(self):
    print("계곡물소리 버튼이 클릭되었습니다!")

  def audio3_btn_clicked(self):
    print("빗소리 버튼이 클릭되었습니다!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
