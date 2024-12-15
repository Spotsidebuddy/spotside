def main():
    amount_due = 50
    accepted_coins = [5, 10, 25]
    while True:
        print('Amount Due:', amount_due)
        coin = get_coin()
        if coin not in accepted_coins:
            continue
        else:
            amount_due -= coin
        if amount_due <= 0:
            print('Change Owed:', -amount_due)
            return

def get_coin():
    coin = int(input('Insert coin: '))
    return coin


if __name__ == '__main__':
    main()
