# Demonstrating built-in data types

a = 10              # int
b = 3.14            # float
c = "Hello"         # string
d = True            # boolean
e = [1, 2, 3]       # list
f = (4, 5, 6)       # tuple
g = {1, 2, 3}       # set
h = {"name": "Abhi", "age": 22}  # dictionary
i = None            # NoneType

variables = [a, b, c, d, e, f, g, h, i]

for var in variables:
    print("Value:", var)
    print("Type:", type(var))
    print("Memory Address:", id(var))
    print("-" * 40)