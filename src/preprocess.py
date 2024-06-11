import re


def preprocess_text(text):
    # Remove unnecessary whitespace and new lines
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text
