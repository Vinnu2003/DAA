def encrypt_vigenere(plaintext, key):
    ciphertext = []
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = key[i % len(key)] % 26  # Modulo to ensure the shift is within A-Z range
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(ciphertext)

if __name__ == "__main__":
    plaintext = "Hello, World!"  # Example plaintext
    key = [3, 19, 5]  # Example key (stream of random numbers)

    encrypted_text = encrypt_vigenere(plaintext, key)
    print("Ciphertext:", encrypted_text)
