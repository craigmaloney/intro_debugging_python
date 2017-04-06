# sum_of_numbers.py

import logging


def main():

    logging.basicConfig(level=logging.INFO)
    list_of_numbers = []
    with open("list_of_numbers", 'rt') as f:
        for number in f:
            try:
                # Convert input to an integer
                list_of_numbers.append(int(number))
            except ValueError:
                logging.warning("Received non-integer input")
                logging.warning(number)

    print("The sum is {total}".format(total=sum(list_of_numbers)))

if __name__ == "__main__":
    main()
