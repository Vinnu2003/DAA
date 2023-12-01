import numpy as np

def hill_cipher(key, plaintext):
    plaintext = ''.join(filter(str.isalpha, plaintext)).lower()
    key = np.array(key)

    while len(plaintext) % 2 != 0:
        plaintext += 'x'  # Padding with 'x' if the length is not divisible by 2

    cipher_text = ''
    for i in range(0, len(plaintext), 2):
        plain_vector = np.array([[ord(char) - ord('a')] for char in plaintext[i:i+2]])
        cipher_vector = np.dot(key, plain_vector) % 26
        cipher_text += ''.join([chr(ciph[0] + ord('a')) for ciph in cipher_vector])
    return cipher_text

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def inverse(key):
    det = int(np.round(np.linalg.det(key))) % 26
    inv = mod_inverse(det, 26)
    adj = np.round(inv * np.linalg.inv(key) * det).astype(int) % 26
    return adj

def hill_decipher(key, ciphertext):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()
    key_inv = inverse(key)

    plain_text = ''
    for i in range(0, len(ciphertext), 2):
        cipher_vector = np.array([[ord(char) - ord('a')] for char in ciphertext[i:i+2]])
        plain_vector = np.dot(key_inv, cipher_vector) % 26
        plain_text += ''.join([chr(plain[0] + ord('a')) for plain in plain_vector])
    return plain_text

def main():
    plaintext = "meetmeattheusualplaceattenratherthaneightoclock"
    key = [[9, 4], [5, 7]]

    print("Original Text:", plaintext)
    cipher_text = hill_cipher(key, plaintext)
    print("Cipher Text:", cipher_text)

    given_ciphertext = "osogunlbhvwghixwvjqmukbwgkqucburhvgrbbvwgzzgb"
    print("\nGiven Ciphertext:", given_ciphertext)
    decrypted_text = hill_decipher(key, given_ciphertext)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
