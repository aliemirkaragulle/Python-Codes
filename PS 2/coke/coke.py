def main():
    inserted_amount = amount()
    remaining = amount_due(inserted_amount)

    while True:
        if remaining > 0:
            print(f"Amount Due: {remaining}")
        else:
            print(f"Change Owed: {-1 * remaining}")
            break
        
        inserted_amount = amount()
        remaining = amount_due(inserted_amount, coke_price = remaining)



def amount():
    while True:
        try:
            amount = int(input("Insert Coin: "))
        except:
            print("Enter a valid integer.")
            break

        if amount in [5, 10, 25]:
            break
        else:
            print("Amount Due: 50")
            continue
    return amount



def amount_due(inserted_amount, coke_price = 50):
    return coke_price - inserted_amount



main()