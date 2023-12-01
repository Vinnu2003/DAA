import string
from collections import Counter

def count_letters(text):
    letter_freq = Counter(c.upper() for c in text if c.isalpha())
    sorted_freq = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_freq

def decrypt_text(ciphertext, frequencies):
    cipher_to_plain = {c: p[0] for c, p in zip(string.ascii_uppercase, frequencies)}
    plaintext = ''.join(cipher_to_plain.get(c, c) for c in ciphertext.upper())
    return plaintext

def main():
    ciphertext = "YourCipherTextHere"  # Replace with the ciphertext

    frequencies = count_letters(ciphertext)
    common_letters = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'  # English letter frequency order

    # Generating potential plaintexts based on frequency analysis
    possible_plaintexts = []
    for i in range(min(10, len(common_letters))):
        common_letter = common_letters[i]
        potential_substitution = frequencies[i][0]
        cipher_to_plain = str.maketrans(potential_substitution, common_letter)
        possible_plaintexts.append(ciphertext.upper().translate(cipher_to_plain))

    print("Top Possible Plaintexts:")
    for plaintext in possible_plaintexts:
        print(plaintext)

if __name__ == "__main__":
    main()
