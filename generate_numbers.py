import random


def main():
    with open("list_of_numbers", 'wt') as f:
        for i in range(1, 2000001):
            f.write(str(random.randint(1, 30000)))
            f.write('\n')
        f.write("Bob\n")

if __name__ == "__main__":
    main()
