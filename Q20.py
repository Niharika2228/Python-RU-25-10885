# Sum of proper divisors of a number

def sum_of_proper_divisors(n):
    total = 1  # 1 is always a proper divisor (for n > 1)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # avoid adding square root twice
                total += n // i
    return total if n > 1 else 0

# Example usage
num = int(input("Enter a number: "))
print("Sum of proper divisors of", num, "is", sum_of_proper_divisors(num))
