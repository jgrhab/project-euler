import numpy as np


MAX_DIGITS = 7  # max index = 1_000_000


def extract_digit(num: int, digit_count: int, digit_idx: int) -> int:
    """Extracts the digit at index `digit_idx` from `num` (from the left).
    `num` should have `digit_count` digits."""

    upper = num // (10 ** (digit_count - digit_idx - 1))
    lower = num // (10 ** (digit_count - digit_idx))

    return upper - 10 * lower


def main():
    # num_counts[d] = number of numbers with d digits
    num_counts = [0] + [digs * 9 * 10 ** (digs - 1) for digs in range(1, MAX_DIGITS)]

    # total_digits[d] = number of digits of all numbers with <= d digits
    total_digits = np.cumsum(num_counts)

    current_idx = 1  # index 1, 10, ..., 1_000_000
    digits_prod = 1  # product of digits at selected indices

    for digit_count in range(MAX_DIGITS):
        while total_digits[digit_count] > current_idx:
            # index of current digit in range of numbers with dig digits
            # subtract 1 to have the indices start at 0
            relative_idx = current_idx - total_digits[digit_count - 1] - 1

            # number containing the digit
            num = 10 ** (digit_count - 1) + relative_idx // digit_count

            digit_idx = relative_idx % digit_count  # index of digit in number

            digits_prod *= extract_digit(num, digit_count, digit_idx)

            current_idx *= 10  # move to next index

    print(digits_prod)


if __name__ == "__main__":
    main()
