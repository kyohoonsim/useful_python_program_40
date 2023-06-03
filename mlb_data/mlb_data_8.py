import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

with sqlite3.connect("lahmansbaseballdb.sqlite") as con:
    cur = con.cursor()
    cur.execute('''
    SELECT playerID, yearID, teamID, ERA FROM pitching WHERE playerID IN ('kershcl01', 'ryuhy01');
    ''')
    result = cur.fetchall()

cols = []
for column in cur.description:
    cols.append(column[0])

df = pd.DataFrame.from_records(data=result, columns=cols)
print(df)

df_ryu = df[df['playerID'] == 'ryuhy01']
print(df_ryu)

df_kershaw = df[df['playerID'] == 'kershcl01']
print(df_kershaw)

plt.plot(df_ryu['yearID'], df_ryu['ERA'], marker='o', markersize=8)
plt.plot(df_kershaw['yearID'], df_kershaw['ERA'], marker='o', markersize=8)
plt.legend(labels=['류현진', '커쇼'], loc='best', fontsize=12)
plt.title('류현진, 커쇼 시즌별 ERA 추이')
plt.xlabel('시즌')
plt.ylabel('ERA')
plt.grid(True)
plt.show()