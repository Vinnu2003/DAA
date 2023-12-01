# Constants for block sizes
CONSTANT_64_BITS = 0x1B
CONSTANT_128_BITS = 0x87

# Function to perform left shift on a value
def left_shift(value, shift_bits, mask):
    shifted = (value << shift_bits) & mask
    overflow = shifted >> 8
    return (shifted ^ (overflow * CONSTANT_64_BITS)) & mask

# Function to generate CMAC subkeys
def generate_cmac_subkeys(block_size):
    if block_size == 64:
        mask = 0xFF
        constant = CONSTANT_64_BITS
    elif block_size == 128:
        mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        constant = CONSTANT_128_BITS
    else:
        raise ValueError("Invalid block size. Supported block sizes are 64 and 128 bits.")

    # Block of all zeros
    block = 0x00

    # Apply block cipher (not implemented here)

    # Generate first subkey
    first_subkey = left_shift(block, 1, mask)

    # Generate second subkey
    second_subkey = left_shift(first_subkey, 1, mask)
    if block_size == 128:
        second_subkey = second_subkey ^ constant

    return first_subkey, second_subkey

# Generating CMAC subkeys for block size 64
subkey_64_1, subkey_64_2 = generate_cmac_subkeys(64)
print("CMAC Subkeys for 64-bit block size:")
print("First Subkey:", hex(subkey_64_1))
print("Second Subkey:", hex(subkey_64_2))

# Generating CMAC subkeys for block size 128
subkey_128_1, subkey_128_2 = generate_cmac_subkeys(128)
print("\nCMAC Subkeys for 128-bit block size:")
print("First Subkey:", hex(subkey_128_1))
print("Second Subkey:", hex(subkey_128_2))
