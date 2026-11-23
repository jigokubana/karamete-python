"""
2.2.Q - Корень зла.
Сложность: Time O(1), Space O(1).
"""


import math


def koren(a: float, b: float, c: float) -> str:
    """Ищет корни"""
    if a == 0 and b == 0 and c == 0:
        return 'Infinite solutions'
    elif a == 0 and b == 0 and c != 0:
        return 'No solution'
    elif a == 0 and b != 0:
        x = -c / b
        return f'{x:.2f}'
    else:
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return 'No solution'
        if discriminant == 0:
            x = -b / (2 * a)
            return f'{x:.2f}'
        else:
            x_one = (-b - math.sqrt(discriminant)) / (2 * a)
            x_two = (-b + math.sqrt(discriminant)) / (2 * a)
            min_x = min(x_one, x_two)
            max_x = max(x_one, x_two)
            return f'{min_x:.2f} {max_x:.2f}'


assert koren(1, -2, 1) == '1.00'
assert koren(3.5, -2.4, -7.3) == '-1.14 1.83'


if __name__ == "__main__":
    a: float = float(input())
    b: float = float(input())
    c: float = float(input())
    print(koren(a, b, c))
