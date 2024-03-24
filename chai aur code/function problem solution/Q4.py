import math
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2* math.pi * radius
    return area,circumference
a ,c = circle(3)
round_off_area = round(a,2)
round_off_circumference = round(c,2)
print(round_off_area , round_off_circumference)