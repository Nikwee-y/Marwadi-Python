# Enrollment No: 92600565001

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

print("Database connected successfully")

db.close()
