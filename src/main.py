from src.decryptor import Decryptor
from src.encryptor import Encryptor


if __name__ == '__main__':

    encryptor = Encryptor()
    decryptor = Decryptor()
    message = encryptor.encrypt("In the evening, ashes fell from the sky.", 3)
    print(message)
    decryptor.dencrypt(message)



