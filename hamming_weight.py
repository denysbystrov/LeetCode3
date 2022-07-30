"""Number 191: Number of 1 bits"""


def hamming_weight(n: int) -> int:
    if n == 0:
        return 0
    return 1 + hamming_weight(n//2) if n % 2 == 1 else 0 + hamming_weight(n//2)

