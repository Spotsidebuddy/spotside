from validator_collection import checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    is_email = checkers.is_email(s)
    if is_email:
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
