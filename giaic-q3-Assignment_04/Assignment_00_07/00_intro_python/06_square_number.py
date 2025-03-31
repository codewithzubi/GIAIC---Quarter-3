# Main function to calculate the square of a number
def main():
    # Taking input from the user for a number they want to square
    num: float = float(input("\033[1;3m Type a number to see its square: \033[0m"))
    
    # Calculating the square of the number and printing the result
    print(str(num), "Squared is ", str(num ** 2))

# Checking if this script is the main program being executed
if __name__ == "__main__":
    # Calling the main function to execute the square calculation
    main()
