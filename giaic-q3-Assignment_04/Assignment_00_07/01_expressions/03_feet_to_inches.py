# Constant for the number of inches in one foot
INCHES_IN_FEET: int = 12

# Main function to convert feet to inches
def main():
    # Ask the user to input a number of feet and convert it to float
    feet: float = float(input("Enter Number of feet: "))
    
    # Calculate the equivalent inches by multiplying feet with the constant INCHES_IN_FEET
    inches: float = feet * INCHES_IN_FEET
    
    # Print the result of conversion, showing how many inches correspond to the given feet
    print("That is", inches, "inches!")

# Ensure the main function is executed if the script is run directly
if __name__ == "__main__":
    main()
