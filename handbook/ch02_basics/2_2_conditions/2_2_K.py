"""
2.2.K - Красота спасёт мир.
Сложность: Time O(1), Space O(1).
"""


def beauty_analysis(number: int) -> str:
    """Проверяет красивое число или нет"""
    a = number // 100
    b = number // 10 % 10
    c = number % 10
    min_d = min(a, b, c)
    max_d = max(a, b, c)
    mid_d = a + b + c - min_d - max_d
    if max_d + min_d == mid_d * 2:
        return 'YES'
    else:
        return 'NO'


assert beauty_analysis(123) == 'YES'
assert beauty_analysis(748) == 'NO'


if __name__ == "__main__":
    number: int = int(input())
    print(beauty_analysis(number))
