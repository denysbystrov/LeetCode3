"""Number 190: Reverse Bits"""


def reverse_bits(n: int) -> int:
    r = 0
    for i in range(32):
        d = n % 2
        n = n//2
        r *= 2
        r += d

    return r
