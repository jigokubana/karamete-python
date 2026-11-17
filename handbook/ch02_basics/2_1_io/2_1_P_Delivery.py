"""
2.1.P - Доставка.
Сложность: Time 0(1), Space 0(1).
"""


def timer(mark_one: int, mark_two: int, speed: int) -> float:
    """Считает за сколько автомобиль доставит товары"""
    return f'{(mark_two - mark_one) / speed:.2f}'


assert timer(10, 32, 5) == '4.40'
assert timer(1, 100, 30) == '3.30'


if __name__ == "__main__":
    mark_one: int = int(input())
    mark_two: int = int(input())
    speed: int = int(input())
    print(timer(mark_one, mark_two, speed))
