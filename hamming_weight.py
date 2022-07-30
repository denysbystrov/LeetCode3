"""Number 191: Number of 1 bits"""


def hamming_weight(n: int) -> int:
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1

    return count

