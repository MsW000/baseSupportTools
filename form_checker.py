import json
import os
from form_validator import validate_form
from report_generator import generate_markdown_report
from database import init_db, save_form

def main():
    init_db() # Инициализация базы до выполнения кода

    data_path = os.path.join("data", "test_forms.json")

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            forms = json.load(f)

        required_fields = ["name", "email", "phone", "message", "city"]
        results = []

        for idx, form in enumerate(forms, start=1):
            result = validate_form(form, required_fields, idx)
            results.append(result)

            if not result["errors"]: # сохраняю результат, если проверка прошла
                save_form(form)

        generate_markdown_report(results)

    except FileNotFoundError:
        print("❌ Файл test_forms.json не найден. Проверь путь.")
    except json.JSONDecodeError:
        print("❌ Ошибка при чтении JSON. Проверь синтаксис файла.")
    except Exception as e:
        print(f"❌ Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()

# forms = [  Перенес в test_forms.json
#     {
#         "name": "Ева",
#         "email": "",
#         "phone": "+7 911 123 45 67",
#         "message": "Хочу узнать про условия",
#         "city": "Минск"
#     },
#     {
#         "name": "Андрей",
#         "email": "andrei@example.com",
#         "phone": "",
#         "message": "",
#         "city": "Гомель"
#     },
#     {
#         "name": "Соня",
#         "email": "sonya@mail.ru",
#         "phone": "+375 33 000 11 22",
#         "message": "Хочу оставить отзыв",
#         "city": "Брест"
#     },
#     {
#         "name": "Адам",
#         "email": "adam@gmail.com",
#         "phone": "+7 911 675 432 10",
#         "message": "Хочу узнать про условия пользователя",
#         "city": "Деревня Бацунь"
#     }
# ]


#requires_fields = ["name", "phone", "city", "message"]

# for numerateForms, form in enumerate(forms, start=1):
#     validate_form(form, requires_fields, numerateForms)

