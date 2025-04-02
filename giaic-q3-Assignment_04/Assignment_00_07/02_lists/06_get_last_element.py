# Function to print the last element of a provided list
def get_last_element(lst):
    """
    Print the Last Element of a Provided list.
    """
    # Print the last element of the list using negative indexing (-1 refers to the last element)
    print(lst[-1])

# Main function to run the program
def main():
    # Example list
    my_list = [10, 20, 30, 40, 50]
    
    # Calling the function to print the last element of the list
    get_last_element(my_list)

# Check if the script is being run directly, if yes, then call the main function
if __name__ == '__main__':
    main()
