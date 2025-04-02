# Main function that runs the program
def main():
    # Define a list of numbers
    numbers: list[int] = [4, 5, 6, 7]

    # Loop through each index in the numbers list using range and len
    for i in range(len(numbers)):
        # Get the element at the current index
        elem_at_index = numbers[i]
        
        # Double the value at the current index and update it in the list
        numbers[i] = elem_at_index * 2
    
    # Print the updated list of numbers, where each number has been multiplied by 2
    print(numbers)

# If this file is run directly, call the main function
if __name__ == "__main__":
    main()
