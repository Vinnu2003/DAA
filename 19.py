from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def cbc_3des_encrypt(plaintext, key, iv):
    backend = default_backend()

    # Pad the plaintext to make its length a multiple of the block size
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return ciphertext

def main():
    # Three 8-byte keys for 3DES (24 bytes in total)
    key_part1 = b'12345678'  # Replace with your 8-byte key
    key_part2 = b'abcdefgh'  # Replace with another 8-byte key
    key_part3 = b'!@#$%^&*'  # Replace with the third 8-byte key

    # Concatenate three 8-byte keys to form a 24-byte key for 3DES
    key_3des = key_part1 + key_part2 + key_part3

    iv = b'IVData123'[:8]  # Initialization Vector (using first 8 bytes)
    plaintext = b"Hello, CBC mode!"  # Input plaintext

    # Encrypt
    ciphertext = cbc_3des_encrypt(plaintext, key_3des, iv)

    # Display results
    print(f"Plaintext: {plaintext.decode('utf-8')}")
    print("Encrypted:", ciphertext.hex())

if __name__ == "__main__":
    main()
