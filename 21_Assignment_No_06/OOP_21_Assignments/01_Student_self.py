class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
       print(f"Hello My Name is {self.name} and my Marks is {self.marks}")
    
obj = Student("Zubair",98)
obj.display()