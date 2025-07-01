import sqlite3
import csv
import os

def export_forms_to_csv():
    os.makedirs("reports", exist_ok=True)
    output_path = os.path.join("reports", "forms.csv")

    conn = sqlite3.connect("db/forms.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM forms")
    rows = cursor.fetchall()

    headers = ["ID", "Name", "Email", "Phone", "Message", "City"]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    conn.close()
    print(f"✅ Экспорт завершён: {output_path}")
