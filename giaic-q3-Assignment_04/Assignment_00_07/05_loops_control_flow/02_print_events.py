def main():
    # The loop will run from 0 to 19 (total 20 iterations)
    for i in range(20):
        # In each iteration, multiply 'i' by 2 to get an even number and print it
        print(i * 2, end=" ")  # 'end=" "' makes the numbers print on the same line with space in between

# This checks if the script is being run directly and calls the main function
if __name__ == "__main__":
    main()  # Call the main function

