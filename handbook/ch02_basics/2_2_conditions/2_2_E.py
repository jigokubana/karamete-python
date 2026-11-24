"""
2.2.E - Яблоки.
Сложность: Time 0(1), Space 0(1).
"""


def golovolomka(v_apples: int, p_apples: int) -> str:
    """Сравнивает кандидатов и выводит победителя."""
    if v_apples > p_apples:
        return 'Петя'
    else:
        return 'Вася'


assert golovolomka(3, 5) == 'Вася'
assert golovolomka(10, 2) == 'Петя'


if __name__ == "__main__":
    v_apples: int = int(input())
    p_apples: int = int(input())
    print(golovolomka(v_apples, p_apples))
