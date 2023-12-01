def add_padding(plaintext, block_size):
    padding_length = block_size - (len(plaintext) % block_size)
    padding = b'\x80' + b'\x00' * (padding_length - 1)
    return plaintext + padding

def remove_padding(padded_text):
    return padded_text.rstrip(b'\x00').rstrip(b'\x80')

# Example usage
block_size = 8  # Block size in bytes (for illustration purposes)
plaintext = b"This is a test message"
padded_text = add_padding(plaintext, block_size)
print("Padded text:", padded_text)
# Now to remove padding at the receiver's end:
original_text = remove_padding(padded_text)
print("Original text:", original_text)
