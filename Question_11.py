# Q11: Tuple packing and unpacking with nested tuples

# Packing: storing multiple values into a tuple
student = ("Abhi", 22, (85, 90, 95))  # nested tuple for marks

print("Packed Tuple:", student)

# Unpacking
name, age, marks = student

print("Name:", name)
print("Age:", age)
print("Marks Tuple:", marks)

# Nested unpacking
m1, m2, m3 = marks

print("Individual Marks:", m1, m2, m3)