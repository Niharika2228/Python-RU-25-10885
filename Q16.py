# Calculate sum of digits of a number

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10   # get last digit
        n //= 10          # remove last digit
    return total

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits of", num, "is", sum_of_digits(num))
