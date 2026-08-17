num = int(input("Enter a number: "))
last_digit = num % 10   # get last digit

if last_digit % 5 == 0:
    print("Last digit is divisible by 5")
else:
    print("Last digit is not divisible by 5")
