"""Number 202: Happy Number"""


def is_happy(n: int) -> bool:
    memo = set()

    while n not in memo:
        if n == 1:
            return True
        memo.update([n])
        result = 0
        while n:
            result += (n % 10) ** 2
            n = n // 10

        n = result

    return False
