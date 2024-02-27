# transportation mode selectyion 
distance = int(input("enter the distance: "))

if distance < 3:
    print("Walk")
elif distance < 15:
    print("Bike")
elif distance > 15:
    print("Car")