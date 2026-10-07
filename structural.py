LATIN = "abcdefghijklmnopqrstuvwxyz"
CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

ALPHABETS = {
    "lat": {"letters": LATIN, "index": {ch: i for i, ch in enumerate(LATIN)}},
    "cyr": {"letters": CYRILLIC, "index": {ch: i for i, ch in enumerate(CYRILLIC)}},
}


def find_alphabet(ch: str) -> dict | None:
    lower = ch.lower()
    for alphabet in ALPHABETS.values():
        if lower in alphabet["index"]:
            return alphabet
    return None


def shift_char(ch: str, k: int) -> str:
    alphabet = find_alphabet(ch)
    if alphabet is None:
        return ch

    letters = alphabet["letters"]
    index = alphabet["index"]
    n = len(letters)

    lower = ch.lower()
    new_pos = (index[lower] + k) % n
    shifted = letters[new_pos]

    return shifted.upper() if ch.isupper() else shifted


def caesar_encrypt(text: str, k: int) -> str:
    return "".join(shift_char(ch, k) for ch in text)


def caesar_decrypt(text: str, k: int) -> str:
    return caesar_encrypt(text, -k)


def is_reversible(text: str, k: int) -> bool:
    return caesar_decrypt(caesar_encrypt(text, k), k) == text


#Демонстрационный сценарий
def main() -> None:
    samples = [
        ("Hello, World! 123", 3),
        ("Привет, Мир! 42", 5),
        ("Mixed: Hello Привет", 7),
    ]

    for text, k in samples:
        encrypted = caesar_encrypt(text, k)
        decrypted = caesar_decrypt(encrypted, k)
        print(f"Исходный:     {text}")
        print(f"Сдвиг:        {k}")
        print(f"Зашифровано:  {encrypted}")
        print(f"Расшифровано: {decrypted}")
        print(f"Обратимо:     {is_reversible(text, k)}")
        print("-" * 45)


if __name__ == "__main__":
    main()