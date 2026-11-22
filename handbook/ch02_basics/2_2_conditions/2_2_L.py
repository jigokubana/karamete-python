"""
2.2.L - Музыкальный инструмент.
Сложность: O(1), O(1).
"""


def triangle_maker(a: int, b: int, c: int) -> str:
    """Проверяет можно ли сложить музыкальный треугольник 3 трубок длиной:"""
    if a + b > c and b + c > a and c + a > b:
        return 'YES'
    else:
        return 'NO'


assert triangle_maker(3, 3, 3) == 'YES'
assert triangle_maker(1, 2, 3) == 'NO'


if __name__ == "__main__":
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    print(triangle_maker(a, b, c))
