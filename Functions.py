#functions are used for reusablity 
#using a function we write a code only once and call it many times
#def keyword is used in python to define a function

#example1
def function_name():
    print("Hello World")  #nothing is happen here

#example2
def painter():
            print("I am a painter")

painter()   #I am a painter / calling function


#example3
def add():
    a=int(input())
    b=int(input())
    print(a+b)

add()  #calling function

sub()  #give error because function is not defined
def sub():
    a=int(input())
    b=int(input())
    print(a-b)

sub()  #calling function

#example4 
#arguments and parameters

def add(a,b):   #a and b are arguments
      print(a+b)

add(5,3) #parameters are 5 and 3

#example5
#conditional statements in function

def findOddOrEven(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

findOddOrEven(4)   #Even
findOddOrEven(7)   #Odd

#example6
#return keyword in function

def printrange(r1,r2):
     for i in range(r1,r2):
         print(i)

printrange(1,11)   #1 2 3 4 5 6 7 8 9 10

#example7
#return keyword in function
#return keyword is used to return a value from a function
def painter():
      return "I am a painter"
      print("painter")  #this line will not execute after return sratement
      
painter()   #nothing happen

msg=painter()  #msg will store the return value of function
print(msg)   #I am a painter

#example8

username="suhas"
password="1234"

un=input("Enter username:")
pw=input("Enter password:")

def validate():
    if un==username and pw==password:
        return True
    else:
        return False
    
a=validate()  #calling function
print(a)   #True or False

#home work Quetions
