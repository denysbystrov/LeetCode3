"""Number 8: String to Integer"""


def my_atoi(s: str) -> int:
    result = 0
    negative = False
    tens_count = 0
    for i in range(len(s)):
        if s[i] == '-':
            negative = True
        elif 48 <= ord(s[i]) <= 57:
            d = int(s[i])
            if tens_count == 9 and result == 214748364:
                if negative:
                    result = 2147483648 if int(d) > 8 else result * 10 + d
                else:
                    result = 2147483647 if int(d) > 7 else result * 10 + d
            else:
                result = result * 10 + d
                tens_count += 1
        else:
            if result > 0:
                break

    return result if not negative else -result

