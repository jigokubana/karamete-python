"""
2.2.N - Властелин Чисел: Две Башни.
Сложность: Time O(1), Space O(1).
"""


def protection(number: int) -> str:
    """Защищает"""
    a = number // 100
    b = number // 10 % 10
    c = number % 10
    weakest = min(a, b, c)
    strongest = max(a, b, c)
    mid = a + b + c - weakest - strongest
    if weakest == 0:
        return f'{mid}{weakest} {strongest}{mid}'
    else:
        return f'{weakest}{mid} {strongest}{mid}'


assert protection(103) == '10 31'
assert protection(787) == '77 87'


if __name__ == "__main__":
    number: int = int(input())
    print(protection(number))
