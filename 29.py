import random

# Function to check if all lanes in the capacity portion have at least one non-zero bit
def all_nonzero(matrix, capacity):
    for row in range(capacity):
        for col in range(capacity):
            if matrix[row][col] != 0:
                return False
    return True

# SHA-3 constants
capacity = 2 * 5  # Capacity in lanes (5 * w)
rate = 24  # Rate in bits

# Internal state matrix
matrix = [[0 for _ in range(capacity)] for _ in range(capacity)]

# Count iterations until all lanes have at least one non-zero bit
iterations = 0
while not all_nonzero(matrix, capacity):
    # Randomly select a lane and set it to a non-zero value (1 bit in this case)
    row = random.randint(0, capacity - 1)
    col = random.randint(0, capacity - 1)
    matrix[row][col] = 1
    iterations += 1

print(f"All lanes have at least one nonzero bit after {iterations} iterations.")
