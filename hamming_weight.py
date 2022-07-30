"""Number 191: Number of 1 bits"""


def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n = n & (n-1)
        count += 1

    return count

