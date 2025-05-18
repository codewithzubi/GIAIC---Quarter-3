# Custom exception class banayi ja rahi hai jo Exception se inherit karti hai
class InvalidAgeError(Exception):
    pass  # isme filhal koi custom logic nahi diya gaya, sirf define kiya gaya hai

# Function banaya gaya hai jo age check karega
def check_age(age):
    if age < 18:
        # agar age 18 se chhoti hai to custom exception raise karega
        raise InvalidAgeError("Age Must Be 18 Above")
    else:
        # agar age valid hai to message print karega
        print("Age is Valid")

# try block mein function ko call kar rahe hain
try:
    check_age(20)  # yahaan age 20 hai, isliye exception nahi raise hoga
except InvalidAgeError as e:
    # agar exception raise hoti hai to usse yahaan handle kiya jaega
    print("Caught an exception:", e)
