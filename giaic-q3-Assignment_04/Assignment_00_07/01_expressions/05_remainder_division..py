# Main function to perform division and calculate quotient and remainder
def main():
    # User se dividend (number to be divided) input le rahe hain aur integer mein convert kar rahe hain
    dividend: int = int(input("\033[1;3m Please enter an integer to be divided: \033[0m"))
    
    # User se divisor (number to divide with) input le rahe hain aur integer mein convert kar rahe hain
    divisor: int = int(input("\033[1;3m Please enter the divisor: \033[0m"))

    # Integer division to calculate the quotient (without decimal)
    quotient: int = dividend // divisor  # Quotient (result of division without remainder)

    # Modulus operator to calculate the remainder
    remainder: int = dividend % divisor  # Remainder after division

    # Final result ko print kar rahe hain: quotient aur remainder ke saath
    print("The Result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# Agar yeh script directly run ho rahi hai toh main() function call ho ga
if __name__ == "__main__":
    main()  # Main function ko call karte hain
