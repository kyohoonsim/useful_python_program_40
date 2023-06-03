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

    layout = QHBoxLayout()
    layout.addWidget(self.audio1_btn)
    layout.addWidget(self.audio2_btn)
    layout.addWidget(self.audio3_btn)

    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
