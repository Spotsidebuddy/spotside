def main():
    file = get_type(input('Input file name: '))
    match file:
        case 'gif':
            print('image/gif')
        case 'jpg' | 'jpeg':
            print('image/jpeg')
        case 'png':
            print('image/png')
        case 'pdf':
            print('application/pdf')
        case 'txt':
            print('text/plain')
        case 'zip':
            print('application/zip')
        case _:
            print('application/octet-stream')

def get_type(file):
    file = file.split('.')
    file = file[-1].lower().strip()
    return file


if __name__ == '__main__':
    main()
