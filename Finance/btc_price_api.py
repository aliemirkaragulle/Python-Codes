import sys
import requests
import json

def main():
    # Number of Bitcoins
    num = get_cla()

    # Price of a Bitcoin
    price = btc_price()

    # Number x Price
    res = (num * price)
    print(f"${res:,.4f}")



def get_cla():
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")

        num = float(sys.argv[1])
        return num

    except ValueError:
        sys.exit("Command-line argument is not a number")



def btc_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()
        # print(json.dumps(response, indent = 2))
        # print(json.dumps(response["bpi"]["USD"]["rate"], indent = 2))

        return response["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        pass

if __name__ == "__main__":
    main()