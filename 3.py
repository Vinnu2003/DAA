import string

def generate_playfair_matrix(key):
    # Create a Playfair matrix based on the given keyword
    key = key.upper().replace('J', 'I')  # Replace 'J' with 'I'
    alphabet = string.ascii_uppercase.replace('J', '')  # Remove 'J' from the alphabet
    matrix = []

    # Initialize the matrix with the keyword
    for char in key:
        if char not in matrix:
            matrix.append(char)

    # Fill the matrix with the remaining letters of the alphabet
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    # Reshape the list into a 5x5 matrix
    matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return matrix

def encrypt_playfair(plaintext, key):
    plaintext = plaintext.upper().replace('J', 'I')  # Replace 'J' with 'I' in the plaintext
    matrix = generate_playfair_matrix(key)

    # Preprocess plaintext to group letters and add padding if needed
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    for i in range(len(plaintext)):
        if len(plaintext[i]) == 1:
            plaintext[i] += 'X'  # Add 'X' to single letters

    ciphertext = ''
    for pair in plaintext:
        char1, char2 = pair[0], pair[1]
        row1, col1, row2, col2 = 0, 0, 0, 0

        # Find positions of chars in the matrix
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char1:
                    row1, col1 = i, j
                if matrix[i][j] == char2:
                    row2, col2 = i, j

        # Encrypt the pair
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

def main():
    plaintext = "HELLO WORLD"
    keyword = "KEYWORD"

    ciphertext = encrypt_playfair(plaintext, keyword)
    print("Plaintext:", plaintext)
    print("Keyword:", keyword)
    print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
