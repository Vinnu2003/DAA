# Define the known mappings
mapping = {
    'B': 'E',  # B likely corresponds to E
    'U': 'T'   # U likely corresponds to T
}

# Find the numerical representation of 'E' and 'T' in ASCII
e_ascii = ord('E') - ord('A')
t_ascii = ord('T') - ord('A')

# Calculate the values of a and b using simultaneous equations
# B corresponds to E: (a * e_ascii + b) % 26 = e_ascii
# U corresponds to T: (a * t_ascii + b) % 26 = t_ascii

# Solve for a
a = (t_ascii - e_ascii) * pow(e_ascii - t_ascii, -1, 26) % 26

# Solve for b
b = (e_ascii - (a * e_ascii)) % 26

print("Keys found: a =", a, "b =", b)
