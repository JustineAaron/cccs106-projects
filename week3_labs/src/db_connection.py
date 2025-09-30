import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",  # 🔑 replace with your real MySQL root password
        database="fletapp"
    )
    return connection
