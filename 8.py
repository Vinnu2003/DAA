import string

# Function to generate the monoalphabetic cipher sequence based on the keyword
def generate_cipher_sequence(keyword):
    keyword = keyword.upper()  # Convert keyword to uppercase
    cipher_seq = list(keyword)

    # Fill the remaining characters in the cipher sequence in normal order
    for char in string.ascii_uppercase:
        if char not in cipher_seq:
            cipher_seq.append(char)

    return ''.join(cipher_seq)

# Function to perform monoalphabetic encryption using the generated cipher sequence
def monoalphabetic_encrypt(cipher_seq, plaintext):
    plaintext = plaintext.upper()  # Convert plaintext to uppercase
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            index = ord(char) - ord('A')
            ciphertext += cipher_seq[index]
        else:
            ciphertext += char  # Keep non-alphabetic characters unchanged

    return ciphertext

def main():
    keyword = "CIPHER"
    plaintext = "Hello, World! This is a monoalphabetic cipher example."

    cipher_sequence = generate_cipher_sequence(keyword)
    print("Generated Cipher Sequence:", cipher_sequence)

    encrypted_text = monoalphabetic_encrypt(cipher_sequence, plaintext)
    print("Plaintext:", plaintext)
    print("Ciphertext:", encrypted_text)

if __name__ == "__main__":
    main()
