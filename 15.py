import string

ALPHABET_SIZE = 26

# Replace the letter_frequencies list with the frequencies of letters in the specific language
# For English, the frequencies could be placed here
letter_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
                      0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
                      0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
                      0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
                      0.01974, 0.00074]

class DecryptionAttempt:
    def __init__(self, shift, score, plaintext):
        self.shift = shift
        self.score = score
        self.plaintext = plaintext

def calculate_score(text, shift):
    score = 0.0
    for char in text:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')
            score += letter_frequencies[index]
    return score

def decrypt_text(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')
            shifted_index = (index - shift + ALPHABET_SIZE) % ALPHABET_SIZE
            plaintext += chr(shifted_index + ord('A'))
        else:
            plaintext += char
    return plaintext

def perform_frequency_attack(ciphertext):
    attempts = []
    for i in range(ALPHABET_SIZE):
        plaintext = decrypt_text(ciphertext, i)
        score = calculate_score(plaintext, i)
        attempts.append(DecryptionAttempt(i, score, plaintext))
    
    return sorted(attempts, key=lambda x: x.score, reverse=True)

def main():
    ciphertext = "YourCiphertextHere"  # Replace with the ciphertext
    
    attempts = perform_frequency_attack(ciphertext)

    print("Top Possible Plaintexts:")
    for i, attempt in enumerate(attempts):
        print(f"Shift {attempt.shift}: Score {attempt.score:.4f}, Plaintext: {attempt.plaintext}")

if __name__ == "__main__":
    main()
