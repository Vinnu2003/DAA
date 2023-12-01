BLOCK_SIZE = 8  # Example block size (in bits)

# Function to pad the plaintext if needed to make it a multiple of the block size
def add_padding(plaintext):
    padding_bits = BLOCK_SIZE - (len(plaintext) % BLOCK_SIZE)
    
    if padding_bits != BLOCK_SIZE:
        padding = '1' + '0' * (padding_bits - 1)  # Padding consists of '1' followed by '0's
        plaintext += padding
    
    return plaintext

if __name__ == "__main__":
    plaintext = "Hello, World!"  # Example plaintext
    padded_plaintext = add_padding(plaintext)

    print("Padded plaintext:", padded_plaintext)
