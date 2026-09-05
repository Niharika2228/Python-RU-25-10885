# Upper pattern
for i in range(1, 6):
    print("   " * (5 - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# Lower pattern
for i in range(5, 0, -1):
    print("   " * (5 - i), end="")
    for j in range(i):
        print(chr(64 + i - j), end=" ")
    print()