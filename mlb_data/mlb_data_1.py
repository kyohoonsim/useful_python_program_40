import sqlite3

with sqlite3.connect("lahmansbaseballdb.sqlite") as con:
    cur = con.cursor()
    cur.execute('''
    SELECT * FROM pitching WHERE playerID = 'ryuhy01';
    ''')
    result = cur.fetchall()

print(result)