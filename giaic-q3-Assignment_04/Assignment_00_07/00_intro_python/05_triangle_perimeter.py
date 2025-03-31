# Main function to calculate the perimeter of a triangle
def main():
    # Taking the length of the first side of the triangle from the user
    side1: float = float(input("\033[1;3m What is the length side 1 ? \033[0m"))
    
    # Taking the length of the second side of the triangle from the user
    side2: float = float(input("\033[1;3m What is the length side 2 ? \033[0m"))
    
    # Taking the length of the third side of the triangle from the user
    side3: float = float(input("\033[1;3m What is the length side 3 ? \033[0m"))

    # Calculating the perimeter by adding all three sides and printing the result
    print(f"The perimeter of the triangle is", str(side1 + side2 + side3))

# Checking if this script is being run as the main program
if __name__ == "__main__":
    # Calling the main function to execute the perimeter calculation
    main()
