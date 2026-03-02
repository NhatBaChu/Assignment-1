import re
def check_course_code(text):
    return bool(re.fullmatch(r"[A-Z]{3}\d{3}", text))
