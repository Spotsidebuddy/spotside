import sys
from datetime import date
import inflect


def main():
    p = inflect.engine()
    try:
        year, month, day = input('Date of Birth: ').split('-')
        minutes = compute(year, month, day)
    except (ValueError, TypeError):
        sys.exit('Invalid date')

    print(f'{p.number_to_words(minutes, andword='').capitalize()} minutes')


def compute(year, month, day):
    today = date.today()
    try:
        bday = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit('Invalid date')
    timedelta = (today - bday).total_seconds()/60
    if timedelta < 0:
        sys.exit('Invalid date')
    return round(timedelta)


if __name__ == '__main__':
    main()
