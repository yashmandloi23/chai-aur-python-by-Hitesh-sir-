# order = str(input("enter your order of coffee: "))
order = "medium"
# extra_short = str(input("would you like to have extra short: "))
extra_short = True
if extra_short:
    coffee = order + " extra short"    
else: 
    coffee = order + " coffee"

print("order is: ", coffee)