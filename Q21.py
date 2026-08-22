# Check if a number is a Happy Number

def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return num == 1

# Example usage
num = int(input("Enter a number: "))
if is_happy(num):
    print(num, "is a Happy Number")
else:
    print(num, "is not a Happy Number")
