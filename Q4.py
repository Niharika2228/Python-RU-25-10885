def last_digit_and_remove(num):
    last_digit = num % 10          # Get the last digit
    remaining = num // 10          # Remove the last digit
    return last_digit, remaining

# Example usage
number = int(input("Enter a number: "))
last, rem = last_digit_and_remove(number)
print("Last digit:", last)
print("Remaining number:", rem)
