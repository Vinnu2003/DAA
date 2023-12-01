import numpy as np

# Function to calculate the inverse of a 2x2 matrix modulo 26
def inverse(key):
    det = key[0, 0] * key[1, 1] - key[0, 1] * key[1, 0]
    inv_det = 0
    
    for i in range(26):
        if (det * i) % 26 == 1:
            inv_det = i
            break

    inverse_key = np.array([
        [key[1, 1], -key[0, 1]],
        [-key[1, 0], key[0, 0]]
    ]) * inv_det % 26

    return inverse_key

# Function to decrypt ciphertext using the key matrix
def decrypt(ciphertext, key):
    inverse_key = inverse(key)
    plaintext = np.dot(inverse_key, ciphertext) % 26
    return plaintext

if __name__ == "__main__":
    known_plaintexts = np.array([[7, 4], [11, 11]])  # Example known plaintexts
    corresponding_ciphertexts = np.array([[19, 7], [1, 6]])  # Example corresponding ciphertexts

    # Calculate the key matrix using known plaintext-ciphertext pairs
    det = np.linalg.det(known_plaintexts)
    inv_det = 0

    for i in range(26):
        if (det * i) % 26 == 1:
            inv_det = i
            break

    key = np.array([
        [(inv_det * known_plaintexts[1, 1]) % 26, ((26 - known_plaintexts[0, 1]) * inv_det) % 26],
        [((26 - known_plaintexts[1, 0]) * inv_det) % 26, (inv_det * known_plaintexts[0, 0]) % 26]
    ])

    # Decrypt ciphertext using the key matrix
    plaintext = decrypt(corresponding_ciphertexts.T, key)
    print("Recovered plaintext:", ''.join(chr(int(x) + 65) for x in plaintext.flatten()))
