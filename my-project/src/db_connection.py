import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",  # 👈 must match the password you set in MySQL
        database="fletapp"
    )
    return connection

