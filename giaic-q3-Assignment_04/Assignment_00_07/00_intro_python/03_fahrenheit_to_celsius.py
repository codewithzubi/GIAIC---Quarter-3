# Main function to convert temperature from Fahrenheit to Celsius
def main():
    # Taking user input for temperature in Fahrenheit
    degrees_fahrenheit = float(input("\033[1;3mEnter Temperature in fahrenheit : \033[0m"))
    
    # Converting Fahrenheit to Celsius using the formula (F - 32) * 5/9
    celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    # Displaying the converted temperature in Celsius
    print(f"Temperature : {degrees_fahrenheit} F = {celsius} C")

# Checking if this script is the main program being executed
if __name__ == "__main__":  
    # Calling the main function to run the program
    main()
