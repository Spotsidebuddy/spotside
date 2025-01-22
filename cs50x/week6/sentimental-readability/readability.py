

def main():
    text = input("Text: ")
    grade = coleman(text)
    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def coleman(text: str) -> int:
    char_count: int = 0
    sentences: int = 0
    words: int = 0

    for i in range(len(text)):
        if text[i].isalpha():
            char_count += 1
        else:
            if text[i-1].isalpha():
                words += 1
            if text[i] in [".", "!", "?"] and text[i-1].isalpha():
                sentences += 1
            if text[i] in ["-", "'"] and text[i+1].isalpha():
                words -= 1

    L: float = (char_count/words)*100
    S: float = (sentences/words)*100
    index: int = round(0.0588 * L - 0.296 * S - 15.8)
    return index


if __name__ == "__main__":
    main()
