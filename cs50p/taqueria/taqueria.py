def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = order_total(menu)
    print(f'Total: $' + '{:.2f}'.format(total))


def order_total(menu):
    cost_total = 0
    while True:
        try:
            item = input('Item: ').strip().title()
            try:
                if item in menu:
                    cost_total += menu[item]
                    print(f"Total: $" + '{:.2f}'.format(cost_total))
            except KeyError:
                continue
            continue
        except EOFError:ьлвшк 
            break
    return cost_total


if __name__ == "__main__":
    main()
