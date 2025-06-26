import re


def _get_after_keyword(text: str, keyword: str) -> str | None:
    pattern = rf"{re.escape(keyword)}\s*(.*)"
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip().splitlines()[0].strip()
    return None


def parse_nombre(text: str) -> str | None:
    """Return the string found after 'Nombre:' in text."""
    return _get_after_keyword(text, "Nombre:")


def parse_cuit(text: str) -> str | None:
    """Return the string found after 'CUIT:' in text."""
    return _get_after_keyword(text, "CUIT:")


def parse_email(text: str) -> str | None:
    """Return the first email found in the text using regex."""
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    if match:
        return match.group(0)
    return None

