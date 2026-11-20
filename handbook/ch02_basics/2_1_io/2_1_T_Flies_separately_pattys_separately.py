"""
Задача: 2.1.T - Мухи отдельно, котлеты отдельно.
Сложность: Time: 0(1), Space 0(1).
"""


def invoice_restorer(n: int, m: int, k1: int, k2: int) -> str:
    """Возвращает веса первой и второй партии котлет"""
    x = int((m * n - n * k2) / (k1 - k2))
    y = int(n - x)
    return f'{x} {y}'


assert invoice_restorer(32, 285, 300, 240) == '24 8'


if __name__ == "__main__":
    n: int = int(input())
    m: int = int(input())
    k1: int = int(input())
    k2: int = int(input())
    print(invoice_restorer(n, m, k1, k2))
