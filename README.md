# baseSupportTools

🎯 Цель проекта

Проект создан как учебно-практический кейс для подготовки к роли поддержки/интеграции. Его задача — отработать:

    чтение JSON,

    валидацию данных,

    логирование и отчётность,

    структурирование Python-кода,

    работу с API и файлами,

    обработку ошибок.

---

## 📦 Функции

- ✅ Валидация анкет (проверка обязательных полей)
- 🧾 Генерация отчётов в Markdown и Excel
- 💾 Сохранение в SQLite
- 📓 Логирование ошибок в файл
- 📊 Мини-аналитика по базе (по городам и e-mail)
- 📤 Экспорт анкет в `.csv` и `.xlsx`

---

## 📁 Структура проекта

SmartSupportTools/ 

├── form_checker.py # Точка входа 
├── form_validator.py # Проверка полей 
├── form_logger.py # Запись ошибок 
├── report_generator.py # Markdown-отчёт 
├── export_to_csv.py # Экспорт в .csv 
├── export_to_excel.py # Экспорт в Excel 
├── stats_report.py # Статистика ├── 

---

## 🚀 Как запустить

1. Установи зависимости:

```bash
pip install openpyxl
```

Запусти основную проверку:

python form_checker.py

Для статистики и экспорта:

python export_to_csv.py
python export_to_excel.py
python stats_report.py
