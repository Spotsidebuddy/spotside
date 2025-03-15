
def main():
    card = input("Card: ")
    if not card.isnumeric() or len(card) not in [13, 15, 16]:
        print("INVALID")
        return
    if not luhn(card):
        print("INVALID")
        return
    if card[:2] in ["34", "37"] and len(card) == 15:
        print("AMEX")
        return
    if card[:2] in ["51", "52", "53", "54", "55"] and len(card) == 16:
        print("MASTERCARD")
        return
    if card[0] == "4" and len(card) in [16, 13]:
        print("VISA")
        return
    else:
        print("INVALID")


def luhn(card):
    s = card[::-1]
    sum = 0
    for i in range(len(s)):
        if i%2 == 1:
            digit = int(s[i])*2
            if digit > 9:
                digit -= 9
        else:
            digit = int(s[i])
        sum += digit
    return sum % 10 == 0



if __name__ == "__main__":
    main()
