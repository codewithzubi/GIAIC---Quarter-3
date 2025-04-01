# Speed of light in meters per second (C)
C: int = 299792458

# Main function to calculate energy from mass
def main():
    # Ask the user to input mass in kilograms and convert it to a float
    mass_in_kg: float = float(input("\033[1;3mEnter Kilos of Mass: \033[0m"))
    
    # Calculate the energy in joules using Einstein's mass-energy equivalence formula (E = m * C^2)
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Print the formula for energy calculation
    print("e = m * C^2...")

    # Print the mass entered by the user
    print("m = " + str(mass_in_kg) + "kg")
    
    # Print the constant speed of light (C)
    print("C = " + str(C) + "m/s")

    # Print the calculated energy in joules
    print(str(energy_in_joules) + " Joules of energy")

# Check if this script is being run directly (not imported)
if __name__ == "__main__":
    main()  # Call the main function to run the program
