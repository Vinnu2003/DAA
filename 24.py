import math

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(e, phi):
    gcd, x, _ = extended_gcd(e, phi)
    if gcd == 1:
        return x % phi

e = 31
n = 3599

# Finding p and q through trial and error
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        p = i
        q = n // i
        break

phi = (p - 1) * (q - 1)

d = mod_inverse(e, phi)

print(f"The private key (d) is: {d}")
