class Product:
    def __init__(self, _price):
        self._price = _price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Price Cannot be negative!!")
    
    @price.deleter
    def price(self):
        print("Deleting Price...")
        del self._price

p = Product(100)
print(p.price)  # 100

p.price = 200   # price update kar diya
print(p.price)  # 200

p.price = -50   # invalid value, error message aayega

del p.price
