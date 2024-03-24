Pet = str(input("enter pet type: "))
Dog_age = int(input("enter the age: "))

if Pet == "dog":
    if age < 3:
        print("puppy food")
    else:
        print("seniour Dog food")
if Pet == "cat":
    if age < 5:
        print("seniour cat food")
    else:
        print("juniour cat food")
