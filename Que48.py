numbers = [1, 0, 2, 0, 3, 4, 0, 5]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

for num in numbers:
    if num == 0:
        result.append(num)

print("List after moving zeros to the end:", result)