"""
Задача: 2.1.N - Шарики и ручки.
Сложность: Time 0(1), Space 0(1)
"""


def turn_analyzer(red_balls: int, blue_balls: int) -> int:
    """
    Возвращает минимальное число шаров для гарантированного
    извлечения зелёного.
    """
    return red_balls + blue_balls + 1


assert turn_analyzer(1, 3) == 5
assert turn_analyzer(2, 6) == 9


if __name__ == "__main__":
    red_balls: int = int(input())
# Пропускаем количество зелёных шаров, так как для худшего случая оно не нужно
    input()
    blue_balls: int = int(input())
    print(turn_analyzer(red_balls, blue_balls))
