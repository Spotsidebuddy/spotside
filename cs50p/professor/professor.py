import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        mistakes_count = 0
        while mistakes_count <= 3:
            if mistakes_count == 3:
                print("EEE")
                print(f'{x} + {y} = {correct_answer}')
                break
            try:
                user_answer = int(input(f'{x} + {y} = '))
            except ValueError:
                print("EEE")
                mistakes_count += 1
                continue
            if user_answer != correct_answer:
                print("EEE")
                mistakes_count += 1
                continue
            if user_answer == correct_answer:
                score += 1
                break

    print(f'Score: {score}')


def get_level():
    while True:
        level = input('Level: ')
        try:
            level = int(level)
            if level in [1, 2, 3]:
                return level
            raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        integer = random.randint(0, 9)
        return integer
    if level == 2:
        integer = random.randint(10, 99)
        return integer
    if level == 3:
        integer = random.randint(100, 999)
        return integer


if __name__ == "__main__":
    main()
