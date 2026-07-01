from file_handler import save_stock
from logger import write_log


def add_fruit(stock):

    fruit = input("Enter Fruit Name : ").title()

    if fruit in stock:
        print("Fruit Already Exists")
        return

    quantity = int(input("Enter Quantity : "))

    price = float(input("Enter Price : "))

    stock[fruit] = {

        "quantity": quantity,

        "price": price

    }

    save_stock(stock)

    write_log(f"Added {fruit}")

    print("Fruit Added Successfully")


def view_stock(stock):

    if len(stock) == 0:

        print("No Stock Available")

        return

    print("\n--------- Stock ---------")

    for fruit, details in stock.items():

        print(

            f"{fruit} | Quantity : {details['quantity']} | Price : ₹{details['price']}"

        )


def update_stock(stock):

    fruit = input("Enter Fruit Name : ").title()

    if fruit not in stock:

        print("Fruit Not Found")

        return

    quantity = int(input("Enter New Quantity : "))

    price = float(input("Enter New Price : "))

    stock[fruit]["quantity"] = quantity

    stock[fruit]["price"] = price

    save_stock(stock)

    write_log(f"Updated {fruit}")

    print("Stock Updated Successfully")