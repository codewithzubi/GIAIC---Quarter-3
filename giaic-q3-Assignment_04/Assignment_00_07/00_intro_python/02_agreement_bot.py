# Main function to interact with the user and display their favorite animal
def main():
    # Taking user input for their favorite animal with bold and italic formatting
    animal = input("\033[1;3m What's your favorite Animal___? \033[0m")

    # Displaying the user's favorite animal in a formatted string
    print(f"My favorite animal is also {animal}!")  # Printing the response in a friendly format

# Calling the main function to execute the code
main()
