import numpy as np


def is_admissible(x: np.int64, y: np.int64, penta: np.ndarray) -> np.bool:
    vals = np.array([x + y, x - y])
    idx = np.searchsorted(penta, vals)

    return (idx < len(penta)).all() and (penta[idx] == vals).all()


BOUND = 5_000


def main():

    ints = np.arange(1, BOUND)

    penta = ints * (3 * ints - 1) / 2
    penta = penta.astype(np.int64)

    pairs = []

    for i in range(len(penta)):
        for j in range(i):
            if is_admissible(penta[i], penta[j], penta):
                pairs.append((penta[i], penta[j]))

    print(pairs[0][0] - pairs[0][1])


if __name__ == "__main__":
    main()
