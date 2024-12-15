import csv
import sys
from tabulate import tabulate


def main():
    filename = get_csv()
    csv_data = parse_csv(filename)
    print(tabulate(csv_data, headers="firstrow", tablefmt="grid"))


def get_csv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many coomand-line arguments")
    filename = sys.argv[1]
    if filename[-3:] != "csv":
        sys.exit("Not a .csv file")
    return filename


def parse_csv(filename):
    prices = []
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                prices.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    return prices


if __name__ == "__main__":
    main()
