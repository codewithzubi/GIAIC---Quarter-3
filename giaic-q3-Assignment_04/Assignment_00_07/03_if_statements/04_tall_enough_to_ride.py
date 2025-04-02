MINIMUM_HEIGHT: int = 50

def main():
    while True:  # Loop ko chalayein jab tak user blank input na de
        height = input("How tall are you? ")  # Height input karayein
        
        if height == "":  # Agar user ne khaali input diya
            break  # Loop ko rok dein
        
        # Agar user ne valid input diya, toh float mein convert karein
        height = float(height)  # Height ko float mein convert karein

        if height >= MINIMUM_HEIGHT:  # Agar height minimum se zyada hai
            print("You're tall enough to ride!")
        else:  # Agar height minimum se kam hai
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
