def main():
    basket = {}
    get_item(basket)
    list_items(basket)

def get_item(basket):
    while True:
        try:
            item = input().upper()
            if item not in basket:
                basket[item] = 1
            else:
                basket[item] += 1

        except EOFError:
            print("\n")
            break

def list_items(basket):
    # Sort Alphabetically by Item
    basket = dict(sorted(basket.items()))

    for k, v in basket.items():
        print(v, k)

main()