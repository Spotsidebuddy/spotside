def main():
    while True:
        date = input("Enter a date: ")
        if '/' in date:
            date = numeric_case(date)
        else:
            date = word_case(date)
        if not date:
            continue
        else:
            print(date)
            break


def numeric_case(date: str):
    # Try parsing the date in the format "9/8/1636"
    try:
        month, day, year = date.split("/")
        month = int(month.strip())
        day = int(day.strip())
        year = year.strip()
        if 1 <= month <= 12 and 1 <= day <= 31 and len(year) == 4:
            try:
                year = int(year)
            except ValueError:
                return False
            return f'{year}-{month:02}-{day:02}'
        else:
            return False
    except ValueError:
        return False


def word_case(date: str):
    # Parsing date in "Month N, Year" format
    if "," not in date:
        return False
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    try:
        month, day, year = date.replace(",", "").split()
        day = int(day)
        if month in months and 1 <= day <= 31 and len(year) == 4:
            year = int(year)
            month = months.index(month) + 1
            return f'{year}-{month:02}-{day:02}'
        else:
            return False
    except ValueError:
        return False


if __name__ == '__main__':
    main()
