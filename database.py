import sqlite3
import os

def init_db():
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect("db/forms.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS forms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            message TEXT,
            city TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_form(form: dict):
    conn = sqlite3.connect("db/forms.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO forms (name, email, phone, message, city)
            VALUES (?, ?, ?, ?, ?)
        """, (
            form.get("name"),
            form.get("email"),
            form.get("phone"),
            form.get("message"),
            form.get("city")
        ))
        conn.commit()

    except sqlite3.IntegrityError:
        print(f"⚠️ Анкета с email '{form.get('email')} уже есть в базе - пропускаем.")
    finally:
        conn.close()