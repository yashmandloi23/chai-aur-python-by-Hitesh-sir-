def print_key(**kargs):
    for key , value in kargs.items():
        print(f"{key}:{value}")
print_key(name = "Shaktiman", power = "laser")
print_key(power = "laser")
print_key(name = "Shaktiman", power = "laser", enemy = "dr.jackaal")
 