def convert(string):
    string = string.replace(':)', '🙂')
    string = string.replace(':(', '🙁')
    return string

def main():
    string = input()
    result = convert(string)
    print(result)


if __name__ == '__main__':
    main()
