from itertools import permutations

def generate_key_square(keyword):
    keyword = keyword.replace('j', 'i').replace('J', 'I')  # Replace 'j' with 'i'
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # Exclude 'j' from the alphabet

    key_square = list(keyword) + [ch for ch in alphabet if ch not in keyword]
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def count_unique_keys(keyword):
    keyword = keyword.lower()
    unique_chars = list(set(keyword.replace('j', 'i')))  # Unique characters in the keyword
    num_unique_chars = len(unique_chars)

    unique_permutations = set(permutations(unique_chars, num_unique_chars))

    return len(unique_permutations)

def main():
    keyword = "PLAYFAIR"  # Example keyword

    key_square = generate_key_square(keyword)
    print("Generated Key Square:")
    for row in key_square:
        print(' '.join(row))

    unique_keys = count_unique_keys(keyword)
    print("\nNumber of Unique Keys (approximate):", unique_keys)

if __name__ == "__main__":
    main()
