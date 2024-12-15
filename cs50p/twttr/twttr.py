def main():
    word = input('Input: ')
    word = shorten(word)
    print(word)


def shorten(string:str) -> str:

    vowels = ['a', 'o', 'u', 'i', 'e']
    result = ''
    for char in string:
        if char.lower() not in vowels :
            result += char
    return result


if __name__ == "__main__":
    main()
