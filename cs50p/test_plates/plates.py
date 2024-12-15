def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    return True if condition_1(plate) and condition_2(plate) and condition_3(plate) and condition_4(plate) else False


def condition_1(string):
    # All vanity plates must start with at least two letters
    str_to_check = string[:2]
    if not string.isupper():
        return False
    for char in str_to_check:
        if is_digit(char):
            return False
    return True


def condition_2(string):
    # Vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters
    return True if 2 <= len(string) <= 6 else False


def condition_3(string):
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # AAA222 would be an acceptable vanity plate;
    # AAA22A would not be acceptable.
    # The first number used cannot be a '0'
    start = -1
    for char in string:
        if is_digit(char):
            start = string.find(char)
            break
    if start != -1:
        string = string[start:]
    if string[0] == '0':
        return False
    for i in range(len(string)):
        if is_digit(string[i]):
            for j in range(i + 1, len(string)):
                if not is_digit(string[j]):
                    return False
    return True


def condition_4(string):
    # No periods, spaces, or punctuation marks are allowed
    no_nos = ['!', '"', '#', '$', '%', '&',
              '\'', '(', ')', '*', '+', ',',
              ' ', '-', '.', '/', ':', ';',
              '<', '=', '>', '?', '@', '[',
              '\\', ']', '^', '_', '`', '{',
              '|', '}', '~']
    for char in string:
        if char in no_nos:
            return False
    return True


def is_digit(string):
    for i in range(10):
        if string == str(i):
            return True
    return False


if __name__ == "__main__":
    main()
