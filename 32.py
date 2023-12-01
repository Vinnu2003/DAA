from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa, rsa, padding

# Generating keys for DSA and RSA
dsa_private_key = dsa.generate_private_key(key_size=1024, backend=default_backend())
rsa_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

message = b"Hello, World!"

# Signing with DSA
dsa_signature1 = dsa_private_key.sign(
    message,
    hashes.SHA256()
)

dsa_signature2 = dsa_private_key.sign(
    message,
    hashes.SHA256()
)

# Signing with RSA
rsa_signature1 = rsa_private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

rsa_signature2 = rsa_private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# Output the signatures
print("DSA Signatures:")
print("Signature 1:", dsa_signature1.hex())
print("Signature 2:", dsa_signature2.hex())
print("DSA signatures are different:", dsa_signature1 != dsa_signature2)

print("\nRSA Signatures:")
print("Signature 1:", rsa_signature1.hex())
print("Signature 2:", rsa_signature2.hex())
print("RSA signatures are same:", rsa_signature1 == rsa_signature2)
