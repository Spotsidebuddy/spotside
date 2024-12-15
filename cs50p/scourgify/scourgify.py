import csv
import sys


def main():
    file_in, file_out = get_filenames()
    students_in = fill_in(file_in)
    full_names = get_fullnames(students_in)
    houses = get_houses(students_in)
    f_names, l_names = parse_fullnames(full_names)
    create_csv_out(file_out)
    write_out(f_names, l_names, houses, file_out)


def get_filenames():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many coomand-line arguments")
    file_in = sys.argv[1]
    if file_in[-3:] != "csv":
        sys.exit("Not a .csv file")
    file_out = sys.argv[2]
    if file_out[-3:] != "csv":
        sys.exit("Output file not a .csv file")
    return [file_in, file_out]


def fill_in(file_in):
    students_in = []
    try:
        with open(file_in) as file:
            names = csv.reader(file)
            for row in names:
                students_in.append(row)
    except FileNotFoundError:
        sys.exit("Input file does not exist")
    return students_in


def get_fullnames(students_in):
    names_out = []
    for student in students_in[1:]:
        names_out.append(student[0])
    return names_out


def get_houses(students_in):
    houses_out = []
    for student in students_in[1:]:
        houses_out.append(student[1])
    return houses_out


def parse_fullnames(names_out):
    f_names = []
    l_names = []
    for student in names_out:
        l_name, f_name = student.split(', ')
        f_names.append(f_name.strip())
        l_names.append(l_name.strip())
    return f_names, l_names


def create_csv_out(file_out):
    columns = ['first', 'last', 'house']
    with open(file_out, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
    return


def write_out(first_names, last_names, houses, file_out):
    with open(file_out, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        for i in range(len(first_names)):
            writer.writerow({'first': first_names[i], 'last': last_names[i], 'house': houses[i]})
    return


if __name__ == "__main__":
    main()
