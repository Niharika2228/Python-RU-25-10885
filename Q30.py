# Binary to Decimal Conversion

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Example usage
binary = input("Enter a binary number: ")
print("Decimal representation of", binary, "is", binary_to_decimal(binary))
