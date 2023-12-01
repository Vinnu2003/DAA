import gmpy2

# Replace these values with your 'n' and known plaintext block
n = 1234567890123456789
plaintext_block = 12345

gcd = gmpy2.gcd(n, plaintext_block)

print(f"GCD of n and the known plaintext block: {gcd}")
