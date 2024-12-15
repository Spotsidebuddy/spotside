def main():
    string = input('camelCase: ')
    normal = camel_to_normal(string)
    snake_case = normal_to_snake(normal)
    print('snake_case:', snake_case)


def camel_to_normal(camel):
    new_string = ''
    camel = camel.strip()
    for char in camel:
        if char.isupper():
            new_string += ' ' + char
        else:
            new_string = new_string + char
        new_string = new_string.strip()
    return new_string


def normal_to_snake(normal):
    normal = normal.lower()
    normal = normal.replace(' ', '_')
    return normal


if __name__ == '__main__':
    main()
