class Bank:
    bank_name = "Meezan Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name


b1 = Bank()
# print(Bank.bank_name)
b1.change_bank_name("Alfala Bank")
print(b1.bank_name)
