import random  # random module ko import karte hain taake hum random numbers generate kar sakein

# Constant variable that defines the number of sides of a dice
NUM_SIDES = 6  # Dice ke sides ka number (6-sided dice)

# Function to simulate rolling two dice
def roll_dice():
    # Rolling two dice and getting a random number between 1 and NUM_SIDES (1 to 6)
    die1: int = random.randint(1, NUM_SIDES)  # First dice roll
    die2: int = random.randint(1, NUM_SIDES)  # Second dice roll
    
    # Calculating the total sum of both dice
    total: int = die1 + die2  
    
    # Printing the total of both dice rolls
    print("Total of two dice", total)

# Main function where the program starts
def main():
    # Initial value of die1 set to 10 (local variable within main function)
    die1: int = 10
    
    # Printing the initial value of die1 before calling roll_dice function
    print("die2 in main() starts as: ", str(die1))
    
    # Calling roll_dice function 3 times to simulate 3 dice rolls
    roll_dice()  # First roll
    roll_dice()  # Second roll
    roll_dice()  # Third roll
    
    # Printing the value of die1 after calling roll_dice function multiple times
    # Notice that die1 remains the same (10) as it's not modified by the roll_dice function
    print("die in main() is :", str(die1))

# Checking if this script is being run directly, and if so, calling the main() function
if __name__ == "__main__":
    main()
