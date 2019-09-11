import sqlite3
connection = sqlite3.connect('warm-up-DB-205.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM tblTry LIMIT 0,30')
row = cursor.fetchall()

for i in row:
    for j in i:
        print(j)

connection.commit()
connection.close()