import os
from datetime import datetime

def generate_markdown_report(result: list):
    os.makedirs("reports", exist_ok=True)
    path = os.path.join("reports", "report.md")

    with open(path, "w", encoding="utf-8") as report:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report.write(f"# 📋 Отчёт по проверке анкет\n")
        report.write(f"_Сформированно: {timestamp}_\n\n")

        for result in result:
            report.write(f"## Анкета {result['number']}\n")
            if result["errors"]:
                report.write("**Ошибка:**\n")
                for error in result("errors"):
                    report.write(f"- ❌ {error}\n")
            else:
                report.write("- ✅ Анкета заполнена корректно\n")
            report.write("\n")