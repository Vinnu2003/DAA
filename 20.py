BLOCK_SIZE = 16

def ecb_encrypt(plaintext, key):
    ciphertext = b''
    for i in range(0, len(plaintext), BLOCK_SIZE):
        block = plaintext[i:i+BLOCK_SIZE]
        # Simulate encryption (replace with your encryption logic)
        encrypted_block = bytes(block[i] ^ key[i % len(key)] for i in range(len(block)))  # XOR operation (for demonstration purposes)
        ciphertext += encrypted_block
    return ciphertext

def ecb_decrypt(ciphertext, key):
    plaintext = b''
    for i in range(0, len(ciphertext), BLOCK_SIZE):
        block = ciphertext[i:i+BLOCK_SIZE]
        # Simulate decryption (replace with your decryption logic)
        decrypted_block = bytes(block[i] ^ key[i % len(key)] for i in range(len(block)))  # XOR operation (for demonstration purposes)
        plaintext += decrypted_block
    return plaintext

def main():
    key = bytes([0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xCD, 0xEF, 0xFE, 0xDC, 0xBA, 0x98, 0x76, 0x54, 0x32, 0x10])
    plaintext = b"Hello, ECB mode!"  # Input plaintext
    
    # Ensure the plaintext length is a multiple of the block size
    extra = len(plaintext) % BLOCK_SIZE
    if extra != 0:
        plaintext += bytes([0] * (BLOCK_SIZE - extra))
    
    # Encrypt
    ciphertext = ecb_encrypt(plaintext, key)
    
    # Decrypt
    decrypted = ecb_decrypt(ciphertext, key)
    
    # Display results
    print(f"Plaintext: {plaintext.decode('utf-8')}")
    print("Encrypted:", " ".join(f"{byte:02X}" for byte in ciphertext))
    print(f"Decrypted: {decrypted.decode('utf-8')}")

if __name__ == "__main__":
    main()
