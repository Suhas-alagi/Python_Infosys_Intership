# Relational Operators(==, !=, <, >, <=, >=)
print(2<5)  #True
print(1<3) #True
print("ABC"=="abc")   #False


#Logical Operators(and, or, not)
"""and =- both conditions should be true
    or =- any one condition should be true
    not =- reverses the result, returns false if the result is true"""
print(2<5 and 1<3)  #True
print(2<5 or 1>3)   #True   
print(not(2<5))     #False


#conditional statements(if, if-else, if-elif-else)
a = 33
b = 200 
if b > a:
  print("b is greater than a")   #b is greater than a
else:
  print("a is greater than b")

#Assignment Operators(=))
x = 5
y = 10  
print(x)  #5
print(y)  #10

#comparisson Operators(==, !=, >, <, >=, <=)
x = 5
y = 10  
print(x == y)  #False
print(x != y)  #True
print(x > y)   #False
print(x < y)   #True
print(x >= y)  #False
print(x <= y)  #True

#Example
india=input("Enter your win or lose: ")

if india=="win":
    print("Trophy is ours")
else:
    print("Better luck next time")


a=int(input())

if (a%5==0 and a%3==0):
    print("Divisible by 3 & 5")
else:
    print("Not Divisible by 3 & 5")
    