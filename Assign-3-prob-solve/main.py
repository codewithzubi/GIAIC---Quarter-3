# 1 - Reverse a string

def reverse_text(text):
    new_text = ""
    for letter in text:
        new_text = letter + new_text   # Add each letter at the beginning
    return new_text

word1 = "Pakistan"
print(word1)                     # Output: Pakistan
print(reverse_text(word1))      # Output: natsikaP

word2 = "Long Live Pakistan"
print(word2)                          # Output: Long Live Pakistan
print(reverse_text(word2))           # Output: natsikaP eviL gnoL

print(reverse_text("apple"))         # Output: elppa



# 2 - Count the number of vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return count

print(count_vowels("Plate"))         # Output: 2



# 3 - Sum of digits in a number (method 1 using for loop)

def sum_digits(number):
    total = 0
    number_str = str(number)         # Convert number to string
    for digit in number_str:
        total += int(digit)          # Convert digit back to integer and add
    return total

print(sum_digits(458743))            # Output: 31



# 3 - Sum of digits in a number (method 2 using while loop)

def add_digits(num):
    total = 0
    while num > 0:
        total += num % 10       # Get last digit
        num = num // 10         # Remove last digit
    return total

print(add_digits(7846815))           # Output: 39
