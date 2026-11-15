"""
2.3.Q - Ошибка кассового аппарата.
Сложность: Time 0(1), Space 0(1).
"""


def perevod(decimal: int, binary: int) -> int:
    """Суммирует уже купленные товары в магазине и сумму последней покупки"""
    binary = int(str(binary), 2)
    return decimal + binary


assert perevod(123, 1101) == 136
assert perevod(783, 10110111) == 966


if __name__ == "__main__":
    decimal: int = int(input())
    binary: int = int(input())
    print(perevod(decimal, binary))