MODULUS = 10_000_000_000
MAX_VALUE = 1000


def main():

    ls = [x**x for x in range(1, MAX_VALUE + 1)]

    print(sum(ls) % MODULUS)


if __name__ == "__main__":
    main()
