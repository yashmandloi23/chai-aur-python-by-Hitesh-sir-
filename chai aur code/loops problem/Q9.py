list = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()
for fruit in list:
    if fruit in unique_item:
        print("duplicate: ", fruit)
        break
    else:
        unique_item.add(fruit)
