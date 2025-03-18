def print_bill(items):
    total = 0
    for item, price in items:
        print(f"{item}: ${price:.2f}")
        total += price
    print(f"Total: ${total:.2f}")

def main():
    items = []
    more_items = True
    while more_items == True:  
        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        items.append((item, price))
        more_items_user = input("Is there more items. Type Yes or No: ")
        if more_items_user == "No":
            more_items = False
    
    print_bill(items)

if __name__ == "__main__":
    main()