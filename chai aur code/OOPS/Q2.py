class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def get_brand(self):
        return self.brand + " !"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
class Ev(car):
        def __init__(self,brand,model,battery_size):
            super().__init__(brand,model)
            self.battery_size = battery_size


my_EV = Ev("tesla","model s","85KWH")

print(my_EV.brand)
print(my_EV.get_brand())

# my_car = car("toyota","innova")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())