"""Number 8: String to Integer"""


def my_atoi(s: str) -> int:
    result = 0
    negative = False
    num_started = False
    for i in range(len(s)):
        if s[i] == '-' or s[i] == "+":
            if num_started:
                break
            num_started = True
            negative = (s[i] == '-')
        elif s[i] == " " and not num_started:
            continue
        elif 48 <= ord(s[i]) <= 57:
            num_started = True
            d = int(s[i])
            if result > 214748364:
                result = 2147483648 if negative else 2147483647
            elif result == 214748364:
                max_digit = 8 if negative else 7
                result = result*10 + max_digit if d > max_digit else result*10 + d
            else:
                result = result*10 + d
        else:
            break

    return result if not negative else -result

