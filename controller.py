from file_handler import load_stock
from fruit_manager import (
    add_fruit,
    view_stock,
    update_stock
)
from customer import buy_fruit


def manager_menu(stock):
    while True:
        print("\n========== Fruit Manager ==========")
        print("1. Add Fruit")
        print("2. View Stock")
        print("3. Update Stock")
        print("4. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_fruit(stock)

        elif choice == "2":
            view_stock(stock)

        elif choice == "3":
            update_stock(stock)

        elif choice == "4":
            break

        else:
            print("Invalid Choice!")


def customer_menu(stock):
    while True:

        print("\n========== Customer ==========")
        print("1. View Fruits")
        print("2. Buy Fruit")
        print("3. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            view_stock(stock)

        elif choice == "2":
            buy_fruit(stock)

        elif choice == "3":
            break

        else:
            print("Invalid Choice!")


def main():

    stock = load_stock()

    while True:

        print("\n========== Fruit Store ==========")
        print("1. Fruit Manager")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            manager_menu(stock)

        elif choice == "2":
            customer_menu(stock)

        elif choice == "3":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main()