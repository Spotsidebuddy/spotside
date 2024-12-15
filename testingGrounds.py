import inflect

p = inflect.engine()


def main():
    word_list = []
    special_chars = "\"\'[]{}!@#$%^&*()-+?_=.;:,<>/|\\"
    flag = False
    while True:
        try:
            word = input('Name: ').strip()
        except EOFError:
            break
        for char in word:
             if char in special_chars:
                flag = True
                break
        if flag:
            print("Please, don't use special characters or punctuation marks in names")
            flag = False
            continue
        if word != "" and not flag:
            word_list.append(word)

    word_list = p.join(word_list, final_sep=",")
    print('Adieu, adieu, to', word_list)


if __name__ == "__main__":
    main()
