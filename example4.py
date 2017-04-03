import logging


# Example 4
def main():

    logging.basicConfig(level=logging.INFO)

    logging.info("Beginning program")

    # Obviously bad code follows
    logging.debug("Beginning Loop")
    for i in range(1, 20):
        i /= 4
        logging.debug(i)
    logging.debug("End Loop")

    if i == 20:
        print("Completed")
        logging.debug("Completed")

    logging.info("End program")

if __name__ == "__main__":
    main()
