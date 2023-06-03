import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("아기 재우기")
    self.setFixedSize(QSize(600, 400))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
