from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Function to perform DES encryption
def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode for simplicity (not recommended for general use)

    # Pad the plaintext to be a multiple of 8 bytes (64 bits)
    padded_plain_text = pad(plain_text.encode(), DES.block_size)

    # Perform encryption
    cipher_text = cipher.encrypt(padded_plain_text)
    return cipher_text

if __name__ == "__main__":
    plaintext = "Hello, World!"  # Example plaintext
    key = get_random_bytes(8)  # Generating a random 64-bit (8 bytes) key

    cipher_text = des_encrypt(plaintext, key)
    print("Cipher Text:", cipher_text.hex())
