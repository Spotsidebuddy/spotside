def main():
    fuel = get_value()
    if fuel >= 99:
        print('F')
    elif fuel <= 1:
        print('E')
    else:
        print(f'{fuel}%')


def get_value():
    while True:
        values = input('Fraction: ').split('/')
        if len(values) != 2:
            # print(f'Incorrect fraction! Should only have 2 args, got {len(values)}')
            continue
        x = values[0]
        y = values[1]
        try:
            x = int(values[0])
            # print(f'x = {x}')
        except ValueError:
            # print('Value Error "x"!')
            continue
        else:
            try:
                y = int(values[1])
                # print(f'y = {y}')
            except ValueError:
                # print('Value Error "y"!')
                continue
            if y < x or y == 0:
                # print("The denominator can't be higher than the numerator!")
                continue
            else:
                values = (x / y) * 100
                percentage = int(round(values, 0))
                # print(percentage)
                return percentage


if __name__ == '__main__':
    main()
