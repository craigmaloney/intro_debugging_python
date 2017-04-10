def pointless_loop(n):

    number_sum = 0
    # This is a pointless loop
    for i in range(1, n+1):
        number_sum += i


def main():
    pointless_loop(30)

if __name__ == '__main__':
    main()
