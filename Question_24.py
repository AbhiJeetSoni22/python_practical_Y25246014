# Q24: Multi-level inheritance

class Grandparent:
    def show1(self):
        print("Grandparent Method")

class Parent(Grandparent):
    def show2(self):
        print("Parent Method")

class Child(Parent):
    def show3(self):
        print("Child Method")

# Usage
obj = Child()
obj.show1()
obj.show2()
obj.show3()