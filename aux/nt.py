import numpy as np


def generate_primes(bound: int) -> np.ndarray[tuple[int], np.dtype[np.int_]]:
    is_prime = np.ones(shape=[bound], dtype=np.bool)
    is_prime[0] = False
    is_prime[1] = False

    for num in range(2, bound):
        if not is_prime[num]:
            continue

        is_prime[np.arange(2 * num, bound, step=num)] = False

    return np.argwhere(is_prime).flatten()


def extend_primes(primes: np.ndarray[tuple[int], np.dtype[np.int_]], bound: int):
    assert primes[-1] < bound

    start = primes[-1] + 1  # start of the new array

    is_prime = np.ones(shape=[bound], dtype=np.bool)
    is_prime[0] = False
    is_prime[1] = False

    is_prime[np.concat([np.arange(2 * pr, bound, pr) for pr in primes])] = False

    for num in range(start, bound):
        if not is_prime[num]:
            continue

        is_prime[np.arange(2 * num, bound, step=num)] = False

    return np.argwhere(is_prime).flatten()
