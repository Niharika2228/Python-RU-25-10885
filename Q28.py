# Sum of first N natural numbers

def sum_natural_numbers(n):
    return n * (n + 1) // 2   # formula-based approach

# Example usage
num = int(input("Enter N: "))
print("Sum of first", num, "natural numbers is:", sum_natural_numbers(num))
