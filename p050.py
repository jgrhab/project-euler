import numpy as np
from collections import defaultdict

from aux import nt

MAX_PRIME = 1_000_000


def main():
    primes = nt.generate_primes(MAX_PRIME)

    # max_seq_len = min index i with 2 + 3 + ... + p_i > primes[-1]
    max_seq_len = np.argwhere(np.cumsum(primes) > primes[-1]).min()

    seqs = defaultdict(list)

    for seq_len in range(21, max_seq_len):
        for idx in range(len(primes) - seq_len):
            seq_sum = primes[idx : idx + seq_len].sum()

            if seq_sum > primes[-1]:
                break

            if primes[np.searchsorted(primes, seq_sum)] == seq_sum:
                seqs[seq_len].append(seq_sum)

    seq_len = max(seqs.keys())

    print(seq_len, ": ", seqs[seq_len])


if __name__ == "__main__":
    main()
