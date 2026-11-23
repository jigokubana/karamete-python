"""
2.2.R - Территория зла.
Сложность: Time O(1), Space O(1).
"""


def evilness_analyzer(n_one: int, n_two: int, n_three: int) -> str:
    c = max(n_one, n_two, n_three)
    a = min(n_one, n_two, n_three)
    b = n_one + n_two + n_three - a - c
    if c ** 2 > a ** 2 + b ** 2:
        return 'велика'
    elif c ** 2 == a ** 2 + b ** 2:
        return '100%'
    else:
        return 'крайне мала'


assert evilness_analyzer(3, 5, 4) == '100%'
assert evilness_analyzer(6, 3, 4) == 'велика'
assert evilness_analyzer(6, 6, 6) == 'крайне мала'


if __name__ == "__main__":
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    print(evilness_analyzer(a, b, c))
