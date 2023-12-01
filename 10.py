# Function to create the Playfair matrix
def create_playfair_matrix(key):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # Exclude 'j' from the alphabet
    key = key.lower().replace('j', 'i')    # Convert to lowercase and replace 'j' with 'i'
    key = ''.join(dict.fromkeys(key))      # Remove duplicate characters

    key_square = key
    for char in alphabet:
        if char not in key_square:
            key_square += char

    playfair_matrix = [key_square[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

# Function to find the positions of characters in the Playfair matrix
def find_position(matrix, ch):
    for i, row in enumerate(matrix):
        if ch in row:
            return i, row.index(ch)
    return -1, -1

# Function to encrypt a message using the Playfair cipher
def playfair_encrypt(matrix, message):
    message = message.lower().replace('j', 'i')  # Convert message to lowercase and replace 'j' with 'i'
    message = ''.join(filter(str.isalpha, message))  # Remove non-alphabetic characters

    # Adjust message (make the length even by adding 'x' at the end if needed)
    if len(message) % 2 != 0:
        message += 'x'

    encrypted_message = ''
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            encrypted_message += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_message += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_message += matrix[row1][col2] + matrix[row2][col1]

    return encrypted_message

# Main function
def main():
    key_matrix = create_playfair_matrix('MFHIJKUNOPQZVWXYELARGDSTBC')
    message = "Must see you over Cadogan West. Coming at once."

    print("Original Message:", message)

    encrypted_message = playfair_encrypt(key_matrix, message)
    print("Encrypted Message:", encrypted_message)

if __name__ == "__main__":
    main()
