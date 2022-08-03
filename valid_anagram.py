"""Number 242: Valid Anagram"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1

    for j in range(len(t)):
        if t[j] not in s_dict:
            return False
        if s_dict[t[j]] == 0:
            return False
        s_dict[t[j]] -= 1

    return True

