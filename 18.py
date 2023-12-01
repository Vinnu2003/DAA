def generate_subkeys(initial_key):
    num_rounds = 16
    subkeys = []

    # Example subsets for modified subkey generation
    subset1 = 0x0FFFFFFF  # Example subset 1 (adjust based on requirements)
    subset2 = 0x0FFFFFFF  # Example subset 2 (adjust based on requirements)

    left = (initial_key >> 28) & subset1
    right = initial_key & subset2

    for round in range(num_rounds):
        left = ((left << 1) | (left >> 27)) & subset1  # First 24 bits from one subset
        right = ((right << 1) | (right >> 27)) & subset2  # Second 24 bits from another subset

        combined = (left << 28) | right
        subkeys.append(combined)

    return subkeys

def main():
    initial_key = 0x123456789ABC  # Replace with your 56-bit key in hex format

    # Generate subkeys
    subkeys = generate_subkeys(initial_key)

    # Display generated subkeys
    print("Generated Subkeys:")
    for i, subkey in enumerate(subkeys, start=1):
        print(f"Round {i:2}: {subkey:012X}")

if __name__ == "__main__":
    main()
