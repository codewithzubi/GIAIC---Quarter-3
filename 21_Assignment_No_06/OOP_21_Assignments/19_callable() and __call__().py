# Multiplier naam ki class banai ja rahi hai
class Multiplier:
    
    # Constructor method jo factor set karta hai jab object banaya jata hai
    def __init__(self, factor):
        self.factor = factor  # factor ko instance variable mein store kiya

    # __call__ method ka matlab hai ke object ko function ki tarah call kiya ja sakta hai
    def __call__(self, number):
        return number * self.factor  # number ko factor se multiply karke return karo

# Multiplier class ka object banaya gaya jiska factor 5 hai
m = Multiplier(5)

# Object ko function ki tarah call kiya gaya, m(10) => 10 * 5 = 50
result = m(10)

# Result ko print kiya gaya
print(result)  # Output: 50

# Ye check karta hai ke kya 'm' callable hai ya nahi (function ki tarah call ho sakta hai ya nahi)
print(callable(m))  # Output: True
