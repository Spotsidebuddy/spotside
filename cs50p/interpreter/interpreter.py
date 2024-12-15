def main():
    expression = input('Enter expression: ').split(' ')
    operation = expression[1]
    x = int(expression[0])
    y = int(expression[2])
    match operation:
        case '+':
            result = x + y
        case '-':
            result = x - y
        case '*':
            result = x * y
        case '/':
            result = x / ycd
    print(float(result))


if __name__ == '__main__':
    main()
