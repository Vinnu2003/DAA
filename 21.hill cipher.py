import numpy as np

class HillCipher:
    def __init__(self, key):
        self.key = key
        self.key_size = int(len(key) ** 0.5)  # Determine the matrix size
        self.key_matrix = self.create_key_matrix()

    def create_key_matrix(self):
        matrix = np.zeros((self.key_size, self.key_size), dtype=int)
        index = 0
        for i in range(self.key_size):
            for j in range(self.key_size):
                matrix[i][j] = self.key[index]
                index += 1
        return matrix

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace(" ", "")
        while len(plaintext) % self.key_size != 0:
            plaintext += "X"
        cipher = ""
        for i in range(0, len(plaintext), self.key_size):
            block = np.zeros((self.key_size, 1), dtype=int)
            for j in range(self.key_size):
                block[j][0] = ord(plaintext[i + j]) % 65
            encrypted_block = np.dot(self.key_matrix, block) % 26
            for j in range(self.key_size):
                cipher += chr(encrypted_block[j][0] + 65)
        return cipher

    def decrypt(self, ciphertext):
        inv_key_matrix = np.linalg.inv(self.key_matrix) % 26
        decipher = ""
        for i in range(0, len(ciphertext), self.key_size):
            block = np.zeros((self.key_size, 1), dtype=int)
            for j in range(self.key_size):
                block[j][0] = ord(ciphertext[i + j]) % 65
            decrypted_block = np.dot(inv_key_matrix, block) % 26
            for j in range(self.key_size):
                decipher += chr(decrypted_block[j][0] + 65)
        return decipher

def main():
    print("Enter the order of the encryption key (e.g., for a 3x3 matrix, enter 9 numbers): ")
    hill_matrix = [int(x) for x in input().split()]

    cipher = HillCipher(hill_matrix)

    option = input("Would you like to encrypt or decrypt some text? (1 or 2)\n1. Encrypt\n2. Decrypt\n")

    if option == "1":
        text_e = input("What text would you like to encrypt: ")
        print("Your encrypted text is:")
        print(cipher.encrypt(text_e))
    elif option == "2":
        text_d = input("What text would you like to decrypt: ")
        print("Your decrypted text is:")
        print(cipher.decrypt(text_d))
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
