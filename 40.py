import re
from collections import Counter
from itertools import permutations

def calculate_frequencies(text):
    # Count letter frequencies in the text
    letters = re.findall('[a-zA-Z]', text.lower())
    freq = Counter(letters)
    total = sum(freq.values())
    freq_percentage = {k: v / total for k, v in freq.items()}
    return freq_percentage

def decrypt(text, key):
    # Decrypt text using the provided key
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += key.get(char, char).lower()
            else:
                decrypted_text += key.get(char.lower(), char.lower()).upper()
        else:
            decrypted_text += char
    return decrypted_text

def frequency_attack(encrypted_text, top_results=10):
    print("Starting frequency attack...")

    # Calculate frequencies of letters in the encrypted text
    frequencies = calculate_frequencies(encrypted_text)
    print("Letter frequencies calculated.")

    # Most common letters in English
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'

    possible_plaintexts = []
    
    # Generate permutations of possible keys based on frequency analysis
    for perm in permutations(common_letters):
        key = {chr(i + ord('a')): perm[i] for i in range(26)}
        plaintext = decrypt(encrypted_text, key)
        possible_plaintexts.append((plaintext, key))

    # Sort possible plaintexts by frequency analysis closeness to English frequencies
    possible_plaintexts.sort(key=lambda x: sum(abs(frequencies.get(c, 0) - calculate_frequencies(x[0]).get(c, 0)) for c in common_letters))
    
    # Print top results
    print("Possible plaintexts (top 10):")
    for result in possible_plaintexts[:top_results]:
        print(f"Plaintext: {result[0]}")

encrypted_text = "Your encrypted text goes here..."
frequency_attack(encrypted_text, top_results=10)
