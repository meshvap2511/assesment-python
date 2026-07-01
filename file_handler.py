import json
import os

FILE_NAME = "fruits.json"


def load_stock():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {}


def save_stock(stock):

    with open(FILE_NAME, "w") as file:
        json.dump(stock, file, indent=4)