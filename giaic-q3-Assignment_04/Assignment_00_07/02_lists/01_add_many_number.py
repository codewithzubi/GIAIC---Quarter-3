# Function to add multiple numbers from a list
def add_many_numbers(numbers) -> int:
    # Initialize total_so_far to 0, which will store the cumulative sum
    total_so_far: int = 0
    
    # Loop through each number in the 'numbers' list
    for number in numbers:
        # Add the current number to the total_sum
        total_so_far += number
    
    # Return the total sum of the numbers
    return total_so_far

# Main function that runs the program
def main():
    # Define a list of numbers to sum
    numbers: list[int] = [1, 2, 3, 4, 5]
    
    # Call the add_many_numbers function to get the sum of numbers in the list
    sum_of_numbers: int = add_many_numbers(numbers)
    
    # Print the result (sum of numbers)
    print(sum_of_numbers)

# If this file is run directly, call the main function
if __name__ == "__main__":
    main()
