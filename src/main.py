from src.decryptor import Decryptor
from src.encryptor import Encryptor


if __name__ == '__main__':

    cypher_loop = True

    while  cypher_loop:
        choice = input("1: Encrypt message\n2: Decrypt message\nOption number: ")
        message = ""
        if choice == "1":
            encryptor = Encryptor()
            message = input("Input the message to decypher: ")
            key = int(input("Input the key: "))
            encryptor.encrypt(message, key)
        elif choice == "2":
            decryptor = Decryptor()
            message = input("Input the message to decypher: ")
            decryptor.dencrypt(message)
        else:
            print("Invalid input!\n")
