from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Function to perform CBC-MAC calculation for a one-block message
def calculate_cbc_mac(key, message):
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\x00' * 16)  # Initialization Vector (IV) set to all zeros
    ciphertext = cipher.encrypt(message)
    return ciphertext[-16:]  # Returning the last block as the MAC

# Function to create X || (X ⊕ T)
def create_modified_message(original_message, cbc_mac):
    xor_result = bytes(a ^ b for a, b in zip(original_message, cbc_mac))
    return original_message + xor_result

# Key for encryption (must be 16 bytes for AES-128)
key = get_random_bytes(16)

# Message X (one-block message)
message_X = b"SecretMsg"

# Pad the message to fit the block size
padded_message = pad(message_X, AES.block_size)

# Calculate CBC-MAC for message X
cbc_mac_X = calculate_cbc_mac(key, padded_message)
print("CBC-MAC for message X:", cbc_mac_X.hex())

# Create X || (X ⊕ T)
modified_message = create_modified_message(padded_message, cbc_mac_X)

# Calculate CBC-MAC for the modified message
cbc_mac_modified = calculate_cbc_mac(key, modified_message)
print("CBC-MAC for X || (X ⊕ T):", cbc_mac_modified.hex())

# Verify if the CBC-MAC for the modified message matches the original CBC-MAC for X
if cbc_mac_modified == cbc_mac_X:
    print("Adversary successfully determined CBC-MAC for X || (X ⊕ T)")
else:
    print("Adversary failed to determine CBC-MAC for X || (X ⊕ T)")
