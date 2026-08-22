# Convert a number to binary representation

def to_binary(n):
    return bin(n).replace("0b", "")

# Example usage
num = int(input("Enter a number: "))
print("Binary representation of", num, "is", to_binary(num))

