# movie ticket pricing 
age = int(input("enter your age: "))
day = str(input("enter todays day: "))
price = 12 if age >= 18 else 8
if day == "wednesday":
    price = price - 2

print("the price of your ticket is:",price)