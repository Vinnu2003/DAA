def generate_vigenere_table():
    table = []
    for i in range(26):
        table.append([chr((j + i) % 26 + ord('A')) for j in range(26)])
    return table

def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper()
    table = generate_vigenere_table()
    ciphertext = ''
    key_idx = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('A')
            ciphertext += table[ord(char) - ord('A')][shift]
            key_idx += 1
        else:
            ciphertext += char

    return ciphertext

def decrypt_vigenere(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper()
    table = generate_vigenere_table()
    plaintext = ''
    key_idx = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('A')
            row = table[shift]
            plaintext += chr(row.index(char) + ord('A'))
            key_idx += 1
        else:
            plaintext += char

    return plaintext

def main():
    plaintext = "Hello, World!"
    key = "KEY"

    encrypted_text = encrypt_vigenere(plaintext, key)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = decrypt_vigenere(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
