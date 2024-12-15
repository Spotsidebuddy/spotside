import emoji as emo


def main():
    str_emoj = input('Input: ')
    print(emo.emojize(str_emoj, language='alias'))


if __name__ == "__main__":
    main()
