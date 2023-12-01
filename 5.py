def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    not_allowed_values = []
    for a in range(26):
        if gcd(a, 26) != 1:
            not_allowed_values.append(a)

    print("Values of a that are not allowed:", not_allowed_values)

if __name__ == "__main__":
    main()
