
class Encryptor:
    """Provides a basic Caesar Cypher encryptor. Skips non-alphabetic characters and lowers the letters"""

    def __init__(self):
        self.alphabetNumber = 26

    def encrypt(self, message: str, key: int):
        result = ""

        for letter in message:
            letter = letter.lower()
            if letter.isalpha():
                result += chr(((ord(letter) - ord("a") + key) % self.alphabetNumber) + ord("a"))
            else:
                result += letter
        print(result)
