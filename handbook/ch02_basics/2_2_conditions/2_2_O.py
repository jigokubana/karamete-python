"""
2.2.O - Властелин Чисел: Возвращение Цезаря.
Сложность: Time O(1), Space O(1).
"""


def strongest_protection(number_one: int, number_two: int) -> str:
    """Собирает из двух двузначных чисел сильнейшее трёхзначное."""
    a = number_one // 10
    b = number_one % 10
    c = number_two // 10
    d = number_two % 10
    strongest = max(a, b, c, d)
    weakest = min(a, b, c, d)
    mid = a + b + c + d - weakest - strongest
    return f'{strongest}{mid % 10}{weakest}'


assert strongest_protection(31, 11) == '321'
assert strongest_protection(49, 17) == '911'
assert strongest_protection(58, 27) == '822'


if __name__ == "__main__":
    number_one: int = int(input())
    number_two: int = int(input())
    print(strongest_protection(number_one, number_two))
