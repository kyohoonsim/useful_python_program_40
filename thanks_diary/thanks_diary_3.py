import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, QAbstractItemView, QLineEdit, QPushButton
import sqlite3
import pandas as pd


def read_data():
    with sqlite3.connect("thanks.db") as con:
        cur = con.cursor()
        cur.execute('''
        SELECT idx, content, created_at FROM thanks_list ORDER BY idx DESC;
        ''')
        result = cur.fetchall()

    cols = []
    for column in cur.description:
        cols.append(column[0])

    thanks_list = pd.DataFrame.from_records(data=result, columns=cols)
    print(thanks_list)

    return thanks_list

def show_data(thanks_list, table):
    table.setRowCount(len(thanks_list))

    for i in range(len(thanks_list)):
        idx = QTableWidgetItem(str(thanks_list.iloc[i, 0]))
        table.setItem(i, 0, idx)
        content = QTableWidgetItem(thanks_list.iloc[i, 1])
        table.setItem(i, 1, content)
        written_at = QTableWidgetItem(thanks_list.iloc[i, 2])
        table.setItem(i, 2, written_at)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("감사일기")
        self.resize(600, 500)
        
        thanks_list = read_data()
        self.table = QTableWidget(len(thanks_list), 3, self) 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['번호', '감사한일', '작성시간'])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        show_data(thanks_list, self.table)

        self.input_text = QLineEdit()
        self.input_btn = QPushButton("입력")
        self.input_btn.clicked.connect(self.input_btn_clicked)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.input_text)
        bottom_layout.addWidget(self.input_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(bottom_layout)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def input_btn_clicked(self):
        new_thanks = self.input_text.text()
        
        if new_thanks:
            with sqlite3.connect("thanks.db") as con:
                cur = con.cursor()
                cur.execute('''
                INSERT INTO thanks_list (content) VALUES (?)
                ''', (new_thanks, ))
                con.commit()

            thanks_list = read_data()
            show_data(thanks_list, self.table)

        self.input_text.setText('')


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()