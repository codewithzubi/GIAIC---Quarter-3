# Parent class A
class A:
    def show(self):
        print("A Class")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("B Class")

# Class C also inherits from A and overrides show()
class C(A):
    def show(self):
        print("C Class")

# Class D inherits from both B and C (Multiple Inheritance)
class D(B, C):
    pass  # No show() method here, so MRO will be used

# Creating object of class D
d = D()

print(D.__mro__ )
# Calling show() - Python will follow MRO: D → B → C → A
# d.show()  # Output: B Class
