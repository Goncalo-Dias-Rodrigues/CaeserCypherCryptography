class Decryptor:
    def __init__(self):
        self.alphabetNumber = 26

    def dencrypt(self, message: str):
        result = ""
        for key in range(0, self.alphabetNumber + 1):
            for letter in message:
                letter = letter.lower()
                if letter.isalpha():
                    result += chr(((ord(letter) - ord("a") - key) % self.alphabetNumber) + ord("a"))
                else:
                    result += letter
            print(f"Key: {key}. Message: {result}")
            result = ""