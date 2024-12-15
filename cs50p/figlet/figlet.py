from pyfiglet import Figlet
import sys
import random

fig = Figlet()


def main():
    font = get_font()
    text = input()
    fig.setFont(font=font)
    fig_text = fig.renderText(text)
    print(fig_text)


def get_font():
    fonts = fig.getFonts()
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in fonts:
                font = sys.argv[2]
                return font
            else:
                print('Invalid usage')
                sys.exit(1)
        elif len(sys.argv) == 2:
            print('Invalid usage')
            sys.exit(1)
        elif len(sys.argv) > 3:
            print('Invalid usage')
            sys.exit(1)
        else:
            print('Invalid usage')
            sys.exit(1)
    except IndexError:
        font = random_font()
        return font



def random_font():
    font_list = fig.getFonts()
    random_range = len(font_list)
    roulette = random.randrange(0, random_range)
    font = font_list[roulette]
    return font


if __name__ == '__main__':
    main()
