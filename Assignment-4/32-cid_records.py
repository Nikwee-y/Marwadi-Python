# Enrollment No: 92600565001

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

c = db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS student(id INT, name VARCHAR(30))")
c.execute("INSERT INTO student VALUES(1, 'Rahul')")
db.commit()

c.execute("SELECT * FROM student")
for x in c.fetchall():
    print(x)

db.close()
