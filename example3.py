import logging


# Example 3
def main():

    logging.basicConfig(filename='example.log', level=logging.DEBUG)

    # Obviously bad code follows
    logging.debug("Beginning Loop")
    for i in range(1, 20):
        i /= 4
        logging.debug(i)
    logging.debug("End Loop")

    if i == 20:
        print("Completed")
        logging.debug("Completed")

    logging.debug("End program")

if __name__ == "__main__":
    main()
