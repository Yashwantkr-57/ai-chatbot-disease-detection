# chatbot/database.py
import sqlite3

DB_NAME = "log.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        message TEXT,
        intent TEXT,
        response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

def log_chat(user_id, message, intent, response):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_logs (user_id, message, intent, response)
    VALUES (?, ?, ?, ?)
    """, (user_id, message, intent, response))

    conn.commit()
    conn.close()


   
