"""
2.2.F - Сила прокрастинации.
Сложность: Time 0(1), Space 0(1).
"""


def leap_year(year: int) -> str:
    """Считает високосный год или нет."""
    if year % 400 == 0:
        return 'YES'
    if year % 100 == 0:
        return 'NO'
    if year % 4 == 0:
        return 'YES'
    return 'NO'


assert leap_year(2020) == 'YES'
assert leap_year(2022) == 'NO'
assert leap_year(1900) == 'NO'
assert leap_year(2000) == 'YES'


if __name__ == "__main__":
    year: int = int(input())
    print(leap_year(year))
