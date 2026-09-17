import encryptor
from src.encryptor import Encryptor


if __name__ == '__main__':

    encryptor = Encryptor()
    print(encryptor.encrypt("Hello There!zZ", 3))


