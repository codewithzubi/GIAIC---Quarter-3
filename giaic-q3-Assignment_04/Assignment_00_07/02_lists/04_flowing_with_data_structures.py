# Function to add 'data' to 'my_list' three times
def add_three_copyes(my_list, data):
    # Loop to append 'data' three times to the list
    for i in range(3):
        my_list.append(data)

# Main function
def main():
    # Asking the user to input a message
    message: str = input("Enter a message to copy: ")
    
    # Creating an empty list to hold the copied messages
    my_list = []
    
    # Printing the list before adding any data
    print("Before List ", my_list)
    
    # Calling the function to add the message three times to the list
    add_three_copyes(my_list, message)
    
    # Printing the list after adding the message
    print("List After ", my_list)

# This checks if the script is being run directly, then calls the main function
if __name__ == '__main__':
    main()
