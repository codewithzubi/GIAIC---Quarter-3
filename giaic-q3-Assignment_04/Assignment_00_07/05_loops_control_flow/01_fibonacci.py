MAX_TERM_VALUE : int = 10000



def main():
    curr_trem = 0
    next_trem = 1

    while curr_trem <= MAX_TERM_VALUE:
        print(curr_trem,end=" ")
        trem_after_next = curr_trem + next_trem
        curr_trem = next_trem
        next_trem = trem_after_next

if __name__ == '__main__':
    main()