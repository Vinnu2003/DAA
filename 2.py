import string

def generate_substitution_key():
    # Generate a random or predefined substitution key
    # For simplicity, let's use a predefined key
    plaintext_alphabet = string.ascii_uppercase
    ciphertext_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
    substitution_key = dict(zip(plaintext_alphabet, ciphertext_alphabet))
    return substitution_key

def encrypt_monoalphabetic(plaintext, key):
    plaintext = plaintext.upper()
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            ciphertext += key[char]
        else:
            ciphertext += char

    return ciphertext

def decrypt_monoalphabetic(ciphertext, key):
    ciphertext = ciphertext.upper()
    plaintext = ''

    # Reverse the key to create a decryption key
    decryption_key = {v: k for k, v in key.items()}

    for char in ciphertext:
        if char.isalpha():
            plaintext += decryption_key[char]
        else:
            plaintext += char

    return plaintext

def main():
    plaintext = "HELLO WORLD"
    
    # Generate a substitution key
    substitution_key = generate_substitution_key()

    # Encrypt the plaintext
    ciphertext = encrypt_monoalphabetic(plaintext, substitution_key)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)

    # Decrypt the ciphertext
    decrypted_text = decrypt_monoalphabetic(ciphertext, substitution_key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
