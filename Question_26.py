# Q26: MySQL connection and insert

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")

# Insert record
cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", ("Abhi", 90))

conn.commit()
print("Record inserted")

conn.close()