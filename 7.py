# Function to decrypt a simple substitution cipher based on character frequency
def decrypt_substitution(ciphertext):
    letter_frequency = {
        'e': 0, 't': 0, 'a': 0, 'o': 0, 'i': 0, 'n': 0, 's': 0, 'h': 0, 'r': 0, 'd': 0,
        'l': 0, 'c': 0, 'u': 0, 'm': 0, 'w': 0, 'f': 0, 'g': 0, 'y': 0, 'p': 0, 'b': 0,
        'v': 0, 'k': 0, 'j': 0, 'x': 0, 'q': 0, 'z': 0
    }

    # Count the frequency of each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            if char in letter_frequency:
                letter_frequency[char] += 1

    # Sort characters by frequency
    sorted_chars = sorted(letter_frequency, key=letter_frequency.get, reverse=True)

    # Substitute characters based on common English letter frequencies
    substitution_dict = {
        'e': sorted_chars[0], 't': sorted_chars[1], 'a': sorted_chars[2],
        'o': sorted_chars[3], 'i': sorted_chars[4], 'n': sorted_chars[5],
        's': sorted_chars[6], 'h': sorted_chars[7], 'r': sorted_chars[8],
        'd': sorted_chars[9]
    }

    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            if char in substitution_dict:
                decrypted_text += substitution_dict[char]
            else:
                decrypted_text += char
        else:
            decrypted_text += char

    return decrypted_text

def main():
    ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 (88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
    decrypted = decrypt_substitution(ciphertext)
    print("Decrypted Message:")
    print(decrypted)

if __name__ == "__main__":
    main()
