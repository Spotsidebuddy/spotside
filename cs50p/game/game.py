import random as r


def main():
    level = get_level()
    real_answer = r.randrange(1, level)
    get_user_answer(real_answer)


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level >= 1:
                return level
            else:
                continue
        except ValueError:
            continue


def get_user_answer(real_answer):
    while True:
        user_answer = input('Guess: ')
        try:
            user_answer = int(user_answer)
        except ValueError:
            continue
        if user_answer > real_answer:
            print('Too large!')
            continue
        elif user_answer < real_answer:
            print('Too small!')
            continue
        else:
            print('Just right!')
            break


if __name__ == "__main__":
    main()
