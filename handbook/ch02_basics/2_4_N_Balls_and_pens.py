"""
Задача: 2.3 (Минимальное количество ходов для гарантированного зелёного шара)
Сложность: Time O(1), Space O(1)
"""


def turn_analyzer(red_balls: int, blue_balls: int) -> int:
    """Возвращает минимальное число шаров для гарантированного извлечения зелёного."""
    return red_balls + blue_balls + 1


assert turn_analyzer(1, 3) == 5
assert turn_analyzer(2, 6) == 9


if __name__ == "__main__":
    red_balls: int = int(input())
    input()  # Пропускаем количество зелёных шаров, так как для худшего случая оно не нужно
    blue_balls: int = int(input())
    print(turn_analyzer(red_balls, blue_balls))