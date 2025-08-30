n = int(input("Enter n: "))

num = 1

print("First Triangle:")
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()



print("Second Triangle:")
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
