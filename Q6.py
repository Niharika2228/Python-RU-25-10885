price = int(input("Enter the bike price: "))

if price <= 50000:
    tax = price * 0.05
elif price <= 100000:
    tax = price * 0.10
else:
    tax = price * 0.15

print("Tax to be paid:", tax)
