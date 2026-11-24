"""
2.2.G - А роза упала на лапу Азора.
Сложность: Time 0(1), Space 0(1).
"""


def polyndrome(number: int) -> str:
    """Проверяет, является ли число полиндромом."""
    a = number // 1000
    b = number // 100 % 10
    c = number // 10 % 10
    d = number % 10
    if a == d and b == c:
        return 'YES'
    else:
        return 'NO'


assert polyndrome(1234) == 'NO'
assert polyndrome(2332) == 'YES'


if __name__ == "__main__":
    number: int = int(input())
    print(polyndrome(number))
