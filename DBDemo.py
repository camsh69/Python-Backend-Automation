import mysql.connector
from utilities.configurations import *

# conn = mysql.connector.connect(
#     host='localhost', database='APIDevelop', user='root', password='root')
conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('SELECT * FROM CustomerInfo')
# row = cursor.fetchone()
# print(row)
# print(row[3])
rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    sum += row[2]
print(sum)
assert sum == 340

query = "UPDATE CustomerInfo SET Location = %s WHERE CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()


conn.close()
