import sys
from PIL import Image, ImageOps


def main():
    file_in, file_out = get_input()
    dress_up(file_in, file_out)


def get_input():
    # if the user does not specify exactly two command-line arguments
    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            sys.exit('Too many command-line arguments')
        if len(sys.argv) < 3:
            sys.exit('Too few command-line arguments')
    file_in, file_out = sys.argv[1].strip(), sys.argv[2].strip()
    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
    extensions = ['.jpg', 'jpeg', '.png']
    if file_in[-4:].lower() not in extensions:
        sys.exit('Invalid input')
    if file_out[-4:].lower() not in extensions:
        sys.exit('Invalid input')
    # if the input’s name does not have the same extension as the output’s name
    if file_in[-3:].lower() != file_out[-3:].lower():
        sys.exit('Input and output have different extensions')
    return file_in, file_out


def dress_up(file_in, file_out):
    try:
        shirt = Image.open('shirt.png')
        head = Image.open(file_in)
    except FileNotFoundError:
        # if the specified input does not exist
        sys.exit('Invalid input')
    size = shirt.size
    head = ImageOps.fit(head, size=size)
    head.paste(shirt, shirt)
    head.save(file_out)


if __name__ == "__main__":
    main()
