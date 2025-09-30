from db_connection import connect_db

conn = connect_db()
cursor = conn.cursor()

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
