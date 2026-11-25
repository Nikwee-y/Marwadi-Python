# Enrollment No: 92600565001

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

c = db.cursor()

c.execute("delete from student where id =1")
db.commit()

c.execute("select * from student")
print(c.fetchall())
