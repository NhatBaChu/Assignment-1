def is_hex_color(text):
    return bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", text))