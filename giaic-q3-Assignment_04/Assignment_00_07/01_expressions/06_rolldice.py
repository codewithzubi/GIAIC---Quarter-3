# Importing the random module to generate random numbers
import random

# Constant defining the number of sides on the dice
NUM_SIDES: int = 6  # Dice ka har side 6 hai (standard dice)

def main():
    # Generating a random number between 1 and NUM_SIDES (inclusive) for the first die
    die1: int = random.randint(1, NUM_SIDES)  # First die roll

    # Generating a random number between 1 and NUM_SIDES (inclusive) for the second die
    die2: int = random.randint(1, NUM_SIDES)  # Second die roll

    # Calculating the total of the two dice rolls
    total: int = die1 + die2  # Total value of both dice rolls

    # Printing out the results of the dice rolls
    print("Dice have", NUM_SIDES, "sides each.")  # Displaying the number of sides on the dice
    print("Second Die :", die2)  # Displaying the value of the second die
    print("Total of two dice :", total)  # Displaying the sum of both dice rolls

# This check ensures the main function runs if the script is executed directly
if __name__ == "__main__":
    main()  # Calling the main function to execute the code
