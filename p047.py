import itertools

import numpy as np

from aux import nt

MAX_PRIME = 500
MAX_MULT = 5


def generate_factors(
    max_prime: int, max_mult: int
) -> np.ndarray[tuple[int, int], np.dtype[np.int_]]:

    primes = nt.generate_primes(max_prime)

    factors_list = []

    for mult in range(4, max_mult + 1):
        fact = np.array(list(itertools.combinations(primes, mult)))  # [_, mult]

        # padding which leaves the product invariant and makes all arrays the same width
        ones = np.ones([fact.shape[0], max_mult - fact.shape[1]], dtype=fact.dtype)

        factors_list.append(np.concat([fact, ones], axis=1))

    return np.concat(factors_list, axis=0)


def main():
    factors = generate_factors(MAX_PRIME, MAX_MULT)
    numbers = np.prod(factors, axis=1)

    print(factors)

    sorted_idx = np.argsort(numbers)
    numbers = numbers[sorted_idx]
    factors = factors[sorted_idx]

    consecutive_idx = [
        idx for idx in range(len(numbers) - 3) if numbers[idx + 3] == numbers[idx] + 3
    ]

    print(len(consecutive_idx))


if __name__ == "__main__":
    main()
