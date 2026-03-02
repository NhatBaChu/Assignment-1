def redact_phone_numbers(text):
    return re.sub(r"(\+84\d+|\b\d{10}\b)", "[REDACTED]", text)