# Constants defining the number of days, hours, minutes, and seconds in a year
DAY_PER_YEAR: int = 365  # Total number of days in a year (assuming a non-leap year)
HOURS_PER_DAY: int = 24  # Number of hours in a day
MIN_PER_HOUR: int = 60  # Number of minutes in an hour
SEC_PER_MIN: int = 60  # Number of seconds in a minute

def main():
    # Calculating the total number of seconds in a year
    total_seconds_in_year: int = DAY_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Printing the result (total seconds in a year)
    print("There are " + str(total_seconds_in_year) + " seconds in a year!")  # Fix: Added str() for the total value

# Running the main function if the script is executed directly
if __name__ == "__main__":
    main()  # Calling the main function
