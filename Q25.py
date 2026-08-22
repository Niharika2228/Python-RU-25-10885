# Generate Fibonacci series up to N terms

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
num = int(input("Enter number of terms: "))
print("Fibonacci series up to", num, "terms:", fibonacci_series(num))
