"""Number 8: String to Integer"""


def my_atoi(s: str) -> int:
    i = 0
    res = 0
    negative = 1

    while i < len(s) and s[i] == " ":
        i += 1

    if i < len(s) and s[i] == "+":
        i += 1
    elif i < len(s) and s[i] == "-":
        negative = -1
        i += 1

    integers = set('0123456789')
    while i < len(s) and s[i] in integers:
        d = int(s[i])
        if res > 214748364:
            return -2147483648 if negative == -1 else 2147483647
        elif res == 214748364:
            max_digit = 8 if negative == -1 else 7
            res = res * 10 + max_digit if d > max_digit else res * 10 + d
        else:
            res = res * 10 + d
        i += 1

    return res*negative



