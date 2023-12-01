import random
import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate a random prime number
def generate_prime():
    prime = random.randint(50, 150)  # Generate a random number between 50 and 150 (example range)
    while not is_prime(prime):
        prime = random.randint(50, 150)
    return prime

# Function to calculate modular exponentiation (base^exp % mod)
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

# Generate new prime numbers p and q
p = generate_prime()
q = generate_prime()
n = p * q  # New modulus

# Calculate Euler's totient function phi(n)
phi = (p - 1) * (q - 1)

# Find a new public key e (commonly chosen as 65537)
e = 65537  # A commonly used value for e

# Calculate private key d using modular inverse
d = 0
while ((d * e) % phi) != 1:
    d += 1

print(f"New Public Key (e, n): ({e}, {n})")
print(f"New Private Key (d, n): ({d}, {n})")
