# Define the voting age for each fictional country
PETURKSBOUIPO_AGE : int = 16  # Voting age in Peturksbouipo
STANLAU_AGE : int = 25        # Voting age in Stanlau
MAYENGUA_AGE : int = 48       # Voting age in Mayengua

def main():
    # Ask the user for their age and convert it to an integer
    user_age = int(input("How Old Are You? "))
    
    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You can not vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
    # Check if the user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")

# This ensures that the main function is only called when the script is run directly
if __name__ == "__main__":
    main()
