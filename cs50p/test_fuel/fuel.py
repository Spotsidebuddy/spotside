def main():
    while True:
        try:
            fuel = input('Fraction: ')
            fuel = convert(fuel)
            fuel = gauge(fuel)
            print(f'{fuel}')
            return
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if y < x:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    percentage = int(percentage)
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    return f'{percentage}%'


if __name__ == "__main__":
    main()
