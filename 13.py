import numpy as np

def determinant(key):
    return np.linalg.det(key)

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def inverse(key):
    det = int(np.round(determinant(key))) % 26
    inv = mod_inverse(det, 26)
    adj = np.round(inv * np.linalg.inv(key) * det).astype(int) % 26
    return adj

def hill_cipher(key, plaintext):
    plaintext = "".join(filter(str.isalpha, plaintext)).lower()
    key = np.array(key)

    while len(plaintext) % 3 != 0:
        plaintext += 'x'  # Padding with 'x' if the length is not divisible by 3

    cipher_text = ''
    for i in range(0, len(plaintext), 3):
        plain_vector = np.array([[ord(char) - ord('a')] for char in plaintext[i:i+3]])
        cipher_vector = np.dot(key, plain_vector) % 26
        cipher_text += ''.join([chr(ciph[0] + ord('a')) for ciph in cipher_vector])
    return cipher_text

def main():
    plaintext = "attackatdawn"
    key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

    print("Plaintext:", plaintext)
    cipher_text = hill_cipher(key, plaintext)
    print("Cipher Text:", cipher_text)

    inverse_key = inverse(key)
    print("\nInverse of the key:")
    print(np.array(inverse_key))

if __name__ == "__main__":
    main()
