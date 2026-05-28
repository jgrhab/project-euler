import numpy as np


def main():
    nums = np.arange(1, 100_000)

    tri = nums * (nums + 1) / 2
    pen = nums * (3 * nums - 1) / 2
    hex = nums * (2 * nums - 1)

    tri = tri.astype(int)
    pen = pen.astype(int)
    hex = hex.astype(int)

    common = np.array([], dtype=int)

    for num in tri:
        if not pen[np.searchsorted(pen, num)] == num:
            continue

        if not hex[np.searchsorted(hex, num)] == num:
            continue

        common = np.append(common, num)

    print(common)


if __name__ == "__main__":
    main()
