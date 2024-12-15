import sys
# i think whis should not count

def main():
    filename = get_filename()
    print(parse_file(filename))


def get_filename():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many coomand-line arguments")
    filename = sys.argv[1]
    if filename[-2:] != "py":
        sys.exit("Not a Python file")
    return filename

def parse_file(filename):
    lines = []
    try:
        with open(filename) as file:
            for line in file:
                if line.lstrip() != "" and line.lstrip()[0] != '#':
                    lines.append(line.lstrip()[0])
    except FileNotFoundError:
        sys.exit("File does not exist")
    return len(lines)


if __name__ == "__main__":
    main()
