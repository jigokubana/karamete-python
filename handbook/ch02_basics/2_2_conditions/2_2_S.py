"""
2.2.S - Территория зла.
Сложность: Time O(1), Space O(1).
"""


def check_zone(x: float, y: float) -> str:
    """Определяет статус зоны по координатам исследователя."""
    if x ** 2 + y ** 2 > 100:
        return 'Вы вышли в море и рискуете быть съеденным акулой!'

    in_top_right = x >= 0 and y >= 0 and x ** 2 + y ** 2 <= 25
    in_top_left = x <= 0 and 0 <= y <= 5 and 3 * y <= 5 * x + 35
    in_bottom = y <= 0 and y >= 0.25 * (x + 1) ** 2 - 9

    if in_top_right or in_top_left or in_bottom:
        return 'Опасность! Покиньте зону как можно скорее!'
    return 'Зона безопасна. Продолжайте работу.'


assert check_zone(3.5, -3.2) == 'Опасность! Покиньте зону как можно скорее!'
assert check_zone(-5.2, 3.4) == 'Зона безопасна. Продолжайте работу.'


if __name__ == "__main__":
    x: float = float(input())
    y: float = float(input())
    print(check_zone(x, y))
