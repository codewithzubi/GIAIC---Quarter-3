# Create Employee class
class Employee:
    # Constructor method
    def __init__(self, name, salary, ssn):
        self.name = name          # public attribute
        self._salary = salary     # protected attribute
        self.__ssn = ssn          # private attribute

# Create object of Employee
emp = Employee("ALI", 22000, 34560654)

print(emp.name)       # access public
print(emp._salary)    # access protected
print(emp.__ssn)      # access private (will give error)
