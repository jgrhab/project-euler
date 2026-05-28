import itertools
import math

from aux import nt

BOUND = 10_000


def main():

    primes = nt.generate_primes(BOUND)
    twice_squares = [2 * x * x for x in range(1, int(math.sqrt(BOUND)))]

    # compute all combinations of the form p + 2 * x^2 (p > 2 so all odd)
    combis = {int(pr + sq) for pr, sq in itertools.product(primes[1:], twice_squares)}

    combis = combis - set(range(BOUND, max(combis)))  # remove values >= BOUND
    combis = combis - set(primes)  # remove primes

    # compute odd composite numbers up to largest combination
    compos = set(range(3, BOUND, 2)) - set(primes)

    diff = compos - combis
    print(min(diff))


if __name__ == "__main__":
    main()
