import re

POLISH_PATTERN = re.compile(r"[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+")

def extract_words(text: str) -> list[str]:
    words = POLISH_PATTERN.findall(text)
    return [word.lower() for word in words]