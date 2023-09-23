

def normalize_str(value: str) -> str:
    return " ".join(map(str.lower, filter(None, value.split(" "))))
