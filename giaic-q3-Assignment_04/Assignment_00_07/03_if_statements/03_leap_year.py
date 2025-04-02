def main():
    # User se year input lene ka prompt
    year = int(input("Please input a year: "))
    
    # Check karna ki year 4 se divide ho raha hai
    if year % 4 == 0:
        
        # Agar year 4 se divide hota hai, ab check karna ki 100 se divide hota hai ya nahi
        if year % 100 == 0:
            
            # Agar year 100 se bhi divide hota hai, phir check karna ki 400 se divide hota hai ya nahi
            if year % 400 == 0:
                print("That's a Leap Year!")  # Agar year 400 se divide ho, toh leap year
            else:
                print("That's not a Leap Year!")  # Agar 400 se divide nahi hota, toh leap year nahi
        else:
            print("That's a leap year!")  # Agar 100 se divide nahi hota, toh leap year hai
    else:
        print("That's not a leap year.")  # Agar year 4 se divide nahi hota, toh leap year nahi

# Ensure program runs only when executed directly
if __name__ == '__main__':
    main()
