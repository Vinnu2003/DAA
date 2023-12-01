def caesar_cipher(text, shift):
    ciphered_text = ''
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Apply Caesar cipher shift for letters
            ciphered_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            ciphered_text += char  # Keep non-alphabetic characters unchanged
    return ciphered_text

def main():
    plaintext = "Hello, World!"

    # Encrypt the plaintext using Caesar cipher for each shift value (1 to 25)
    for shift in range(1, 26):
        ciphertext = caesar_cipher(plaintext, shift)
        print(f"Shift {shift}: {ciphertext}")

if __name__ == "__main__":
    main()
