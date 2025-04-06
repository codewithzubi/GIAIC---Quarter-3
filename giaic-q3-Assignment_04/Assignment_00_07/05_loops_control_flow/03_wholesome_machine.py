# Define the affirmation string that the user has to type correctly
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    # Print the message asking the user to type the given affirmation
    print("Please type the following affirmation: " + AFFIRMATION)

    # Take user input and store it in 'user_feedback' variable
    user_feedback = input()

    # Loop until the user types the correct affirmation
    while user_feedback != AFFIRMATION:
        # If the user input is incorrect, prompt them again
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again
        print("Please type the following affirmation: " + AFFIRMATION)

        # Take user input again
        user_feedback = input()
    
    # Once the user types the correct affirmation, print the success message
    print("That's Right! :)")

# This checks if the script is being run directly and calls the main function
if __name__ == "__main__":
    main()  # Call the main function
