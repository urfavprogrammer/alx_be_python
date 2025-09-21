pattern = int(input("Enter the size of the pattern: "))
i =0

while i < pattern:
    for n in range(0, pattern):
        print("*", end="")
    print()
    i += 1