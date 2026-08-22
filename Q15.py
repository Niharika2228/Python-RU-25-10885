# Find the largest prime factor of a number

def largest_prime_factor(n):
    # Start with the smallest prime
    factor = 2
    largest = 1
    
    while n > 1:
        if n % factor == 0:
            largest = factor
            n //= factor
        else:
            factor += 1
    return largest

# Example usage
num = int(input("Enter a number: "))
print("Largest prime factor of", num, "is", largest_prime_factor(num))
