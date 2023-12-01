# S-DES encryption function
def sdes_encrypt(plaintext_block, key):
    # Your S-DES encryption logic here
    # ...

    # Example implementation (replace this with your S-DES logic)
    encrypted_block = "encrypted"  # Placeholder for encryption

    return encrypted_block


# Counter Mode (CTR) encryption
def counter_mode(plaintext, key, counter):
    encrypted = ""
    block_size = 8  # Assuming a block size of 8 bits (for S-DES)

    for i in range(0, len(plaintext), block_size):
        plaintext_block = plaintext[i:i+block_size]
        encrypted_counter = sdes_encrypt(format(counter, '08b'), key)
        
        # XOR plaintext block with encrypted counter
        encrypted_block = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(plaintext_block, encrypted_counter))
        encrypted += encrypted_block

        # Increment counter for the next block
        counter += 1

    return encrypted


# Test data
plaintext = "000000010000001000000100"  # Binary plaintext
key = "0111111101"  # Binary key
counter = 0  # Counter starting at 0

encrypted = counter_mode(plaintext, key, counter)
print("Encrypted:", encrypted)
