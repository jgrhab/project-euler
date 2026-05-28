import itertools
from aux import nt


def generate_primes_in_interval(lower: int, upper: int):
    """Generates primes `lower` < p <= `upper`."""

    primes_lower = nt.generate_primes(lower)
    primes_upper = nt.extend_primes(primes_lower, upper)

    return primes_upper[len(primes_lower) :]


def get_digits_4d_number(num: int) -> list[int]:
    digits = [0] * 10

    for _ in range(3):
        nxt = num // 10
        digits[num - 10 * nxt] += 1
        num = nxt

    digits[num] += 1

    return digits


def main():

    # generate all 4-digits primes
    primes = generate_primes_in_interval(1000, 10_000)

    triples = [
        (int(p1), int(p2), int(p3))
        for (p1, p2) in itertools.combinations(primes, 2)
        if (p3 := 2 * p2 - p1) in primes
    ]

    admissible_triples = []

    for p1, p2, p3 in triples:
        digits = get_digits_4d_number(p1)

        if digits != get_digits_4d_number(p2):
            continue

        if digits != get_digits_4d_number(p3):
            continue

        admissible_triples.append((p1, p2, p3))

    print(admissible_triples)


if __name__ == "__main__":
    main()
