import sqlite3
from collections import Counter
import os

def generate_stats():
    conn = sqlite3.connect("db/forms.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM forms")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT city FROM forms")
    cities = [row[0] for row in cursor.fetchall()]
    city_counts = Counter(cities)

    cursor.execute("SELECT email FROM forms")
    domains = [email.split("@")[1] for email in cursor.fetchall() if "@" in email[0]]
    domain_counts = Counter(domains)

    conn.close()

    print(f"\n📊 Статистика по базе:")
    print(f"- Всего анкет: {total}")

    print(f"\n🏙️ Распределение по городам:")
    for city, count in city_counts.items():
        print(f"  {city}: {count}")

    print(f"\n📧 E-mail домены:")
    for domain, count in domain_counts.items():
        print(f"  {domain}: {count}")