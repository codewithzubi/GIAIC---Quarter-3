def main():
    fruits ={
    "apple":25,
    "durian":30,
    "jackfruit":37,
    "kiwi":39,
    "rambutan":12,
    "mango":33}

    total_cost = 0;
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("\033[1;3mHow many (" + fruit_name + ") do you want to buy?: \033[0m"))
        total_cost += (price * amount_bought)
    print("Your total is $" + str(total_cost))


if __name__ == '__main__':






    main()


