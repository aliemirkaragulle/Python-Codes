menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0

    while True:
        try:
            food = input("Item: ").title()
            total_cost += menu[food]
            print(f"Total: ${total_cost:.2f}")

        except EOFError:
            print("\n")
            break
        except KeyError:
            print("No such food on the menu!")
        except:
            pass

main()