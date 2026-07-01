import logging

logging.basicConfig(

    filename="transactions.log",

    level=logging.INFO,

    format="%(asctime)s - %(message)s"

)


def write_log(message):

    logging.info(message)