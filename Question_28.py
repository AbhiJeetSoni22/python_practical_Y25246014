# Q28: Update and delete

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)

cursor = conn.cursor()

# Update
cursor.execute("UPDATE students SET marks=95 WHERE name='Abhi'")

# Delete
cursor.execute("DELETE FROM students WHERE name='Abhi'")

conn.commit()
conn.close()

print("Update and Delete done")