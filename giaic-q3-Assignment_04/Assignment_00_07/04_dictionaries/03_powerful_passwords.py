from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    
    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    
    # Hashing the input password and checking if it matches the stored hash for this email
    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    
    Inputs:
        password: the password we want to hash
    
    Outputs:
        the hashed form of the input password
    """
    # Converting password into bytes and applying sha256 hashing
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # Hash of "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Hash of "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # Hash of "123!456?789"
    }
    
    # Test login with different emails and passwords
    print(login("example@gmail.com", stored_logins, "word"))  # Expected: False, wrong password
    print(login("example@gmail.com", stored_logins, "password"))  # Expected: True, correct password
    
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # Expected: True, correct password
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Expected: False, case-sensitive
    
    print(login("student@stanford.edu", stored_logins, "password"))  # Expected: False, wrong password
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # Expected: True, correct password

if __name__ == '__main__':
    main()
