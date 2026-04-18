# Q25: Class variables vs Instance variables

class Student:
    # 🔹 Class Variable (shared by all objects)
    school_name = "ABC School"

    def __init__(self, name, marks):
        # 🔹 Instance Variables (unique for each object)
        self.name = name
        self.marks = marks


# Creating objects
s1 = Student("Abhijeet", 85)
s2 = Student("Rahul", 90)

# Accessing instance variables
print("Student 1:", s1.name, s1.marks)
print("Student 2:", s2.name, s2.marks)

# Accessing class variable
print("School (s1):", s1.school_name)
print("School (s2):", s2.school_name)

# Modify class variable
Student.school_name = "XYZ School"

print("\nAfter changing class variable:")
print("School (s1):", s1.school_name)
print("School (s2):", s2.school_name)

# Modify instance variable (only for one object)
s1.name = "Amit"

print("\nAfter changing instance variable:")
print("Student 1 name:", s1.name)
print("Student 2 name:", s2.name)