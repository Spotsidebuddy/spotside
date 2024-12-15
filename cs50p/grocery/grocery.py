def main():
    the_list = get_list()
    for key in sorted(the_list.keys()):
        print(the_list[key], key)


def get_list():
    item_list = {}
    while True:
        try:
            item = input().upper()
            # something wrong with input here: if no prompt all works
            # if prompt = prints prompt before printing out list
        except EOFError:
            return item_list
        if item in item_list:
            item_list[item] += 1
        else:
            item_list[item] = 1


if __name__ == '__main__':
    main()
