def main():
    lst = []

    val = input("Enter a Value: ")
    while val:
        lst.append(val)
        val = input("Enter a Value: ")
    print("Here's the list:", lst)

if __name__ == '__main__':
    main()