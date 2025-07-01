# 📄 form_logger.py
import os

def log_error(form_number: int, field: str):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)  # создаём папку, если её нет

    log_path = os.path.join(log_folder, "errors.log")
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"[Анкета {form_number}] Отсутствует поле: {field}\n")
