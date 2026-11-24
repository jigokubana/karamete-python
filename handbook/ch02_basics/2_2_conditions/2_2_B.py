"""
2.2.B - Кто быстрее?
Сложность: Time 0(1), Space 0(1).
"""


def winner_finder(first_candidate: int, second_candidate: int) -> str:
    """Находит победителя путём сравнения."""
    if first_candidate > second_candidate:
        return 'Петя'
    else:
        return 'Вася'


assert winner_finder(10, 5) == 'Петя'
assert winner_finder(5, 7) == 'Вася'


if __name__ == "__main__":
    first_candidate: int = int(input())
    second_candidate: int = int(input())
    print(winner_finder(first_candidate, second_candidate))
