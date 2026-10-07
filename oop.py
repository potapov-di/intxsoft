class Alphabet:

    def __init__(self, letters: str) -> None:
        self._letters = letters
        self._index = {ch: i for i, ch in enumerate(letters)}

    def contains(self, ch: str) -> bool:
        return ch.lower() in self._index

    def shift(self, ch: str, k: int) -> str:
        lower = ch.lower()
        n = len(self._letters)
        new_pos = (self._index[lower] + k) % n
        shifted = self._letters[new_pos]
        return shifted.upper() if ch.isupper() else shifted


class CaesarCipher:

    def __init__(self, alphabets: list[Alphabet]) -> None:
        self._alphabets = alphabets

    def _shift_char(self, ch: str, k: int) -> str:
        for alphabet in self._alphabets:
            if alphabet.contains(ch):
                return alphabet.shift(ch, k)
        return ch  # символ вне алфавитов — оставляем как есть

    def encrypt(self, text: str, k: int) -> str:
        return "".join(self._shift_char(ch, k) for ch in text)

    def decrypt(self, text: str, k: int) -> str:
        return self.encrypt(text, -k)

    def is_reversible(self, text: str, k: int) -> bool:
        return self.decrypt(self.encrypt(text, k), k) == text


#Демонстрационный сценарий
def main() -> None:
    cipher = CaesarCipher([
        Alphabet("abcdefghijklmnopqrstuvwxyz"),
        Alphabet("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
    ])

    samples = [
        ("Hello, World! 123", 3),
        ("Привет, Мир! 42", 5),
        ("Mixed: Hello Привет", 7),
    ]

    for text, k in samples:
        encrypted = cipher.encrypt(text, k)
        decrypted = cipher.decrypt(encrypted, k)
        print(f"Исходный:     {text}")
        print(f"Сдвиг:        {k}")
        print(f"Зашифровано:  {encrypted}")
        print(f"Расшифровано: {decrypted}")
        print(f"Обратимо:     {cipher.is_reversible(text, k)}")
        print("-" * 45)


if __name__ == "__main__":
    main()