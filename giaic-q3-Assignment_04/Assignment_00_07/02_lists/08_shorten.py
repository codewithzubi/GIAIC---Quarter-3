# Define the maximum length allowed for the list
MAX_LENGTH: int = 3

# Function to shorten the list by removing elements from the end
def shorten(lst):
    """
    Removes elements from the end of the list until the list is MAX_LENGTH long.
    """
    # While the list length is greater than MAX_LENGTH, remove and print elements from the end
    while len(lst) > MAX_LENGTH:
        # Remove the last element of the list
        last_elem = lst.pop()
        # Print the removed element
        print(last_elem)

# Function to get a list of elements from the user
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    # Initialize an empty list to store the user input
    lst = []
    # Prompt the user to enter the first element
    elem = input("Please enter an element of the list or press enter to stop. ")
    
    # Keep asking for user input until the user presses Enter without entering any element
    while elem != "":
        # Add the entered element to the list
        lst.append(elem)
        # Prompt the user to enter the next element
        elem = input("Please enter an element of the list or press enter to stop. ")
    
    # Return the list of elements entered by the user
    return lst

# Main function to execute the program logic
def main():
    # Get the list of elements from the user
    lst = get_lst()
    # Shorten the list by removing elements from the end and printing them
    shorten(lst)

# Ensure that the main function runs when the script is executed directly
if __name__ == '__main__':
    main()
