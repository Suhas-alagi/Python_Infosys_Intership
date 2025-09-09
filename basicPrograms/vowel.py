s = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)