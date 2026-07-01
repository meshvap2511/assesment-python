from file_handler import save_stock
from logger import write_log


def buy_fruit(stock):

    if len(stock) == 0:
        print("No Fruits Available")
        return

    print("\nAvailable Fruits")

    for fruit, details in stock.items():

        print(f"{fruit} - Qty : {details['quantity']} - Price : ₹{details['price']}")

    fruit = input("\nEnter Fruit Name : ").title()

    if fruit not in stock:
        print("Fruit Not Found")
        return

    quantity = int(input("Enter Quantity : "))

    if quantity <= 0:
        print("Invalid Quantity")
        return

    if quantity > stock[fruit]["quantity"]:
        print("Not Enough Stock Available")
        return

    total = quantity * stock[fruit]["price"]

    stock[fruit]["quantity"] -= quantity

    save_stock(stock)

    write_log(f"Customer Purchased {quantity} Kg {fruit} | Bill = ₹{total}")

    print("\nPurchase Successful")
    print("Total Bill = ₹", total)