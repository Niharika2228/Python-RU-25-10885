# Reverse digits of a number

def reverse_digits(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10   # add last digit to reversed number
        n //= 10                  # remove last digit
    return rev

# Example usage
num = int(input("Enter a number: "))
print("Reversed number is:", reverse_digits(num))
