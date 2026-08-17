def check_divisible_by_7(num):
    if num % 7 == 0:
        return "Divisible by 7"
    else:
        return "Not divisible by 7"

# Example usage
number = int(input("Enter a number: "))
print(check_divisible_by_7(number))
