# Check if a number is Automorphic

def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

# Example usage
num = int(input("Enter a number: "))
if is_automorphic(num):
    print(num, "is an Automorphic number")
else:
    print(num, "is not an Automorphic number")
