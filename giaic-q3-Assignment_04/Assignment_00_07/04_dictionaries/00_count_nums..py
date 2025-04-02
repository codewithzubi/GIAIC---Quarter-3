def get_users_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break

        num = int(user_input)
        user_numbers.append(num)
    return user_numbers
def count_nums():
    num_dict = {}
    for num in num_dict:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " tiems. ")

def main():
    user_numbers = get_users_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()