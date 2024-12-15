def main():
    time = input('What time is it? ')
    time = convert(time)
    if 7 <= time <= 8:
        print('breakfast time')
    if 12 <= time <= 13:
        print('lunch time')
    if 18 <= time <= 19:
        print('dinner time')

def convert(time):
    x, y = time.split(':')
    x.strip()
    y.strip()
    x = int(x)
    if 'p.m.' in y:
        x = x + 12
    if 'a.m.' or 'p.m.' in y:
        y = y[:2]
    y = int(y)/60
    y = round(y, 2)
    time = x + y
    return float(time)


if __name__ == "__main__":
    main()
