# Function to get and print the first element of the provided list
def get_first_element(lst):
    """
    Print the First Element of a Provided list.
    """
    # Print the first element of the list (index 0)
    print(lst[0])

# Function to get user input to form a list
def get_lst():
    """
    Prompts the user to enter one element of the list at a time 
    and returns the resulting list when the user presses enter to stop.
    """
    lst = []  # Initialize an empty list to store user inputs
    # Get the first input from the user
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    
    # Keep asking for input until the user presses enter without entering anything
    while elem != "":  # Continue if the user hasn't pressed enter (empty input)
        lst.append(elem)  # Add the element to the list
        elem = input("Please enter an element of the list or press enter to stop. ")  # Ask for next input
    
    return lst  # Return the complete list after user stops inputting

# Main function to drive the program logic
def main():
    lst = get_lst()  # Get the list of elements from the user
    get_first_element(lst)  # Print the first element of the list

# Check if the script is being run directly, if yes, then call the main function
if __name__ == '__main__':
    main()
