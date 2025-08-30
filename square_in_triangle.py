n = int(input("Enter a number: "))
start = 1
for i in range(n):
    for j in range(n):
        print(start, end=" ")
        start += 1
    print()
