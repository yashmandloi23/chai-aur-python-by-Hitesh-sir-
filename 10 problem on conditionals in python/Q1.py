age = int(input("enter a age: "))
if age < 13:
    print("child")
elif age < 19:
    print("teenager") 
elif age < 59:
    print("adult")
else:
    print("seniour")