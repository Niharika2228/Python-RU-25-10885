# Count trailing zeros in factorial of a number

def count_trailing_zeros(n):
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

# Example usage
num = int(input("Enter a number: "))
print("Number of trailing zeros in", num, "factorial is:", count_trailing_zeros(num))
