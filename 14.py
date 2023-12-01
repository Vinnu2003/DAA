def encrypt(plaintext, key):
    ciphertext = ''
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.islower():
                shift = (ord(char) - ord('a') + key[i]) % 26
                ciphertext += chr(shift + ord('a'))
            else:
                shift = (ord(char) - ord('A') + key[i]) % 26
                ciphertext += chr(shift + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if char.islower():
                shift = (ord(char) - ord('a') - key[i] + 26) % 26
                decrypted_text += chr(shift + ord('a'))
            else:
                shift = (ord(char) - ord('A') - key[i] + 26) % 26
                decrypted_text += chr(shift + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    plaintext = "sendmoremoney"
    key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

    ciphertext = encrypt(plaintext, key)
    print("Encrypted Text:", ciphertext)

    # The provided ciphertext from the encrypted "sendmoremoney" message
    given_ciphertext = "cashnotneeded"

    # To find the key for decryption to "cashnotneeded"
    key_to_decrypt = []
    for i in range(len(given_ciphertext)):
        shift = (ord(given_ciphertext[i]) - ord(plaintext[i])) % 26
        key_to_decrypt.append(shift)

    decrypted_text = decrypt(given_ciphertext, key_to_decrypt)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
