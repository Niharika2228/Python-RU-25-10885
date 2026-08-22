# Count set bits in binary representation

def count_set_bits(n):
    count = 0
    while n > 0:
        count += n & 1   # check last bit
        n >>= 1          # shift right
    return count

# Example usage
num = int(input("Enter a number: "))
print("Number of set bits in", num, "is", count_set_bits(num))
