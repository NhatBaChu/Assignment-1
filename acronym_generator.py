def acronym(text):
    result = ""
    for word in text.split():
        result += word[0].upper()
    return result
