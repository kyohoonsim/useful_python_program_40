import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

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

plt.plot(df['yearID'], df['ERA'])
plt.title('류현진 시즌별 ERA 추이')
plt.xlabel('시즌')
plt.ylabel('ERA')
plt.grid(True)
plt.show()