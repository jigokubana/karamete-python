"""
2.3.R - Сдача 10.
Сложность: Time 0(1), Space 0(1).
"""


def change(itemcost: int, denomination: int) -> int:
    """Подсчитывает сдачу, которую требуется отдать пользователю"""
    itemcost = int(str(itemcost), 2)
    return denomination - itemcost


assert change(1001001, 100) == 27
assert change(101111100, 500) == 120


if __name__ == "__main__":
    itemcost: int = int(input())
    denomination: int = int(input())
    print(change(itemcost, denomination))