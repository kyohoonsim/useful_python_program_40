import sqlite3
import pandas as pd

with sqlite3.connect("lahmansbaseballdb.sqlite") as con:
    cur = con.cursor()
    cur.execute('''
    SELECT playerID, yearID, teamID, W, L, G, SV, IPouts, ERA, SO, BB, H FROM pitching WHERE playerID = 'ryuhy01';
    ''')
    result = cur.fetchall()

cols = []
for column in cur.description:
    cols.append(column[0])

df = pd.DataFrame.from_records(data=result, columns=cols)
print(df)

df1 = df[['W', 'L', 'ERA', 'SO', 'BB', 'H']]

df1_statistics = df1.describe()
print(f"[류현진 기록 기초통계량]\n{df1_statistics}")