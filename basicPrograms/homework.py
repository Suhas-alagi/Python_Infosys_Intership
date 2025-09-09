# Program to print only alphabets from a given string

s = input("Enter a string: ")

for i in s:
    if i.isalpha():   
        print(i, end="")


# Program to print only uppercase letters from a given string

s = input("Enter a string: ")

for i in s:
    if i.isupper():   
        print(i, end="")


# Calculator in Python

print("Welcome to Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if ch == "1":
    print("Result =", num1 + num2)
elif ch == "2":
    print("Result =", num1 - num2)
elif ch == "3":
    print("Result =", num1 * num2)
elif ch == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice")
