from db_connection import connect_db

try:
    conn = connect_db()
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Error:", e)
