#write function with show_numbers that takes number N and print all the numbers frm 0 to N with label to identify the even and odd numbers 
 

def show_numbers(N):
    for i in range(N+1):
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

N = int(input("Enter a number: "))
show_numbers(N) 


#write a program that checks if N is b/w 200 and 500  print yes if N is b/w 200 and 500 . otherwise print No

def check_number(N):
    if 200 <= N <= 500:
        print("YES")
    else:
        print("NO")

N = int(input("Enter a number: "))
check_number(N) 

#Write a function with the name get weather_report that takes the temperature as an argument. If the temperature is less than 22, it should return "Cold". -If the temperature is greater than or equal to 22 and less than 35, it should return "Warm". - If the temperature is greater than or equal to 35, it should return "Hot".

def get_weather_report(temp):
    if temp < 22:
        return "Cold"
    elif 22 <= temp < 35:
        return "Warm"
    else:
        return "Hot"
    
temp = float(input("Enter the temperature: "))
report = get_weather_report(temp)
print("Weather report:", report)

