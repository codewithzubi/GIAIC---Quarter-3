# Function to add two numbers
def add():
    # Taking the first number as input from the user and converting it to integer
    num1: str = input("Enter a number you want to add: ")
    num1 = int(num1)  # Converting input to integer

    # Taking the second number as input from the user and converting it to integer
    num2: str = input("Enter a number you want to add: ") 
    num2 = int(num2)  # Converting input to integer

    # Calculating the total sum of both numbers
    total: int = num1 + num2

    # Displaying the result of the addition
    print("The sum of", num1, "and", num2, "is", total)

# Calling the add function to execute the code
add()
