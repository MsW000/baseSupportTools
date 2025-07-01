# Добавил код просмотра базы данных через python.
import sqlite3

def view_all_forms():
    conn = sqlite3.connect("db/forms.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM forms")
    rows = cursor.fetchall()

    for row in rows:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Email: {row[2]}")
        print(f"Phone: {row[3]}")
        print(f"Message: {row[4]}")
        print(f"City: {row[5]}")
        print("------")

    conn.close()

if __name__ == "__main__":
    view_all_forms()