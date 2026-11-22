"""
2.2.M - Властелин Чисел: Братство общей цифры.
Сложность: Time O(1), Space O(1).
"""


def digit_analyzer(a: int, b: int, c: int) -> int:
    """Вычисляет какая цифра у трёх чисел одинаковая"""
    if a % 10 == b % 10 == c % 10:
        return a % 10
    else:
        return a // 10


assert digit_analyzer(12, 13, 14) == 1
assert digit_analyzer(23, 13, 63) == 3


if __name__ == "__main__":
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    print(digit_analyzer(a, b, c))
