n = int(input("Enter num: "))

fact = 1
for i in range(1, n+1):
    fact *= i

print("Factorial of", n, "is:", fact)
