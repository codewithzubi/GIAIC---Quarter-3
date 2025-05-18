# Base class Person
class Person:
    # Constructor for Person
    def __init__(self, name):
        self.name = name  # public attribute

# Derived class Teacher from Person
class Teacher(Person):
    # Constructor for Teacher
    def __init__(self, name, subject):
        super().__init__(name)     # call Person's constructor
        self.subject = subject     # new attribute for Teacher

# Create object of Person
p1 = Person("Usman")
print(p1.name)  # prints Usman's name

# Create object of Teacher
t1 = Teacher("Zubair", "Computer Science")
print(t1.name, t1.subject)  # prints Zubair and his subject
