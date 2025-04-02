import random  # Random module ko import karte hain, jo random numbers generate karne mein help karega

# Number of random numbers jo humein generate karne hain
N_NUMBERS : int = 10  
# Minimum value jo hum random number generate karte waqt use karenge
MIN_VALUE : int = 1  
# Maximum value jo hum random number generate karte waqt use karenge
MAX_VALUE : int = 100

def main():
    # Loop chalane ka maksad 10 random numbers generate karna hai
    for i in range(N_NUMBERS):  # Loop runs for N_NUMBERS times (10 times in this case)
        # Random number generate karte hain range (1, 100) se
        numbers = random.randint(MIN_VALUE, MAX_VALUE)
        # Generated number ko print karte hain space ke saath
        print(numbers, end=" ")

# Yeh condition check karta hai agar script directly run ho rahi ho (not imported as module)
if __name__ == "__main__":  
    main()  # main function ko call karte hain jab script directly run ho
