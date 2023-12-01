def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def encrypt(message, e, n):
    encrypted_chars = []
    for char in message:
        plaintext = ord(char) - ord('A')  # Convert character to numeric representation (0-25)
        encrypted = mod_exp(plaintext, e, n)  # RSA encryption
        encrypted_chars.append(encrypted)
    return encrypted_chars

# Sample RSA parameters
p = 61  # Prime number 1
q = 53  # Prime number 2
n = p * q  # Modulus
e = 17  # Public exponent

# Plain text message
message = "HELLO"
print(f"Original Message: {message}")

# Encrypting the message
encrypted_message = encrypt(message, e, n)
for i, encrypted in enumerate(encrypted_message):
    print(f"Encrypted char {message[i]}: {encrypted}")
