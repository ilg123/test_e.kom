import re
from datetime import datetime

def is_email(value):
    return re.match(r"[^@]+@[^@]+\.[^@]+", value) is not None

def is_phone(value):
    return re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value) is not None

def is_date(value):
    for date_format in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError:
            continue
    return False

def detect_field_type(value):
    if is_date(value):
        return "date"
    elif is_phone(value):
        return "phone"
    elif is_email(value):
        return "email"
    else:
        return "text"
