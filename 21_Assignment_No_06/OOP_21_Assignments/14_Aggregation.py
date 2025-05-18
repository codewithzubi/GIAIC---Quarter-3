# Department class
class Department:
    def __init__(self, name):
        self.name = name  # department name

# Employee class with department info
class Employee:
    def __init__(self, employee):
        self.employee = employee  # store Department object

# Create Department object
dprt = Department("Zubair")

# Create Employee object and pass department
emp = Employee(dprt)

# Access department name through employee object
print(emp.employee.name)  # Output: Zubair

