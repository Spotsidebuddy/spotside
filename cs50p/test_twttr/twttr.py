def main():
    word = input('Input: ')
    word = shorten(word)
    print(word)


def shorten(word):
    vowels = ['a', 'o', 'u', 'i', 'e']
    result = ''
    for char in word:
        if char.lower() not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()
