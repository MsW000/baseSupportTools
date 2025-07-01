from form_logger import log_error

def validate_form(form: dict, required_fields: list, form_number: int) -> dict:
    print(f"\n🧾 Анкета {form_number}")
    errors = []

    for field in required_fields:
        value = form.get(field, "")
        if not value.strip():
            print(f" ⚠️ {field} — отсутствует")
            log_error(form_number, field)
            errors.append(f"{field} - отсутствует")
        else:
            print(f" ✅ {field}: {value}")

    if not errors:
        print(" ✅ Анкета заполнена корректно")

    return {
        "number": form_number,
        "errors": errors
    }