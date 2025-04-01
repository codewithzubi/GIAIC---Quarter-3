import math  # Math module ko import karte hain taake hum mathematical calculations kar sakein, jaise square root.

def main():
    # User se AB aur AC ki lengths input kar rahe hain
    ab: float = float(input("\033[1;3m Enter the length of AB: \033[0m"))  # AB ki length input karte hain
    ac: float = float(input("\033[1;3m Enter the length of AC: \033[0m"))  # AC ki length input karte hain

    # Pythagoras Theorem ka use karke BC ki length (hypotenuse) calculate karte hain
    # Formula: BC^2 = AB^2 + AC^2 ==> BC = sqrt(AB^2 + AC^2)
    bc: float = math.sqrt(ab**2 + ac**2)  # AB aur AC ki lengths ke square ka sum lete hain aur uski square root lete hain

    # Hypotenuse BC ki length ko print karte hain
    print("The length of BC (the hypotenuse) is: " + str(bc))  # BC ki length ko output karte hain

# Yeh check karta hai ki script directly run ho rahi hai ya nahi
if __name__ == "__main__":  # Agar script directly run ho rahi hai, toh main() function ko call karte hain
    main()  # main() function ko call karte hain
