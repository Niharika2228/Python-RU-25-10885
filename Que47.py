list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60]

result = []

for item in list1:
    if item not in list2:
        result.append(item)

print("Elements present in first list but not in second:", result)
