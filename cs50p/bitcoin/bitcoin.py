import requests
import sys


def main():
    n = get_n()
    price = get_current_price()
    cost = n * price
    print(f"${cost:,.4f}")


def get_n():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        n = float(sys.argv[1])
        return n

    except ValueError:
        sys.exit("Comand-line argument is not a number")


def get_current_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    except requests.RequestException:
        sys.exit("Could not reach CoinDesk API")

    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    return price


if __name__ == "__main__":
    main()
