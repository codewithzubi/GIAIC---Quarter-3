def main():
    # User se ek number input kar rahe hain aur usse integer mein convert kar rahe hain
    user_input = int(input("Please Input Number You to: "))

    # curr_value ko user_input ke barabar initialize kar rahe hain
    curr_value = user_input 

    # Jab tak curr_value 100 se kam hai, loop chalega
    while curr_value < 100:
        # current value ko print kar rahe hain, end=" " se numbers ek hi line mein aayenge
        print(curr_value, end=" ")

        # curr_value ko double kar rahe hain
        curr_value = curr_value * 2

# Ye line program ko main function call karne ke liye use hoti hai jab script run ho
if __name__ == "__main__":
    main()
