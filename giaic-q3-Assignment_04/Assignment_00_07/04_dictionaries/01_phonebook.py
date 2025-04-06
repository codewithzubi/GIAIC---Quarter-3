def read_phone_numbers():
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        numbers = input("Number: ")
        phonebook[name] = numbers
    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    while True:
        name = input("Enter Name to Lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is note in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


if __name__ == '__main__':
    main()
