def main():
    greeting = 'Greeting: '
    money = value(greeting)
    print(f'${money}')


def value(greeting):
    greeting = input("Greetings: ").strip().lower()
    if 'hello' in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

