import random

def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def generate_large_prime():
    while True:
        num = random.randint(2**19, 2**20)
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            return num

prime_modulus = generate_large_prime()
base = random.randint(2, prime_modulus - 1)

secret_Alice = random.randint(1, prime_modulus - 2)
secret_Bob = random.randint(1, prime_modulus - 2)

public_Alice = mod_exp(base, secret_Alice, prime_modulus)
public_Bob = mod_exp(base, secret_Bob, prime_modulus)

shared_secret_Alice = mod_exp(public_Bob, secret_Alice, prime_modulus)
shared_secret_Bob = mod_exp(public_Alice, secret_Bob, prime_modulus)

print(f"Shared secret for Alice: {shared_secret_Alice}")
print(f"Shared secret for Bob: {shared_secret_Bob}")
