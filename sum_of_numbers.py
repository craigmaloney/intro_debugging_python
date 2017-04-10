# sum_of_numbers.py


def main():

    list_of_numbers = []
    with open("list_of_numbers", 'rt') as f:
        for number in f:
            list_of_numbers.append(number)

    print("The sum is {total}".format(total=sum(list_of_numbers)))

if __name__ == "__main__":
    main()
