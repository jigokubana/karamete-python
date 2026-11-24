"""
2.2.D - Список победителей.
Сложность: Time O(1), Space O(1).
"""


def winners_list(p_speed: int, v_speed: int, t_speed: int) -> str:
    """Сравнивает кандидатов и выводит их в виде списка строк."""
    if p_speed >= v_speed and p_speed >= t_speed:
        if v_speed >= t_speed:
            return '1. Петя\n2. Вася\n3. Толя'
        else:
            return '1. Петя\n2. Толя\n3. Вася'
    elif v_speed >= p_speed and v_speed >= t_speed:
        if p_speed >= t_speed:
            return '1. Вася\n2. Петя\n3. Толя'
        else:
            return '1. Вася\n2. Толя\n3. Петя'
    else:
        if p_speed >= v_speed:
            return '1. Толя\n2. Петя\n3. Вася'
        else:
            return '1. Толя\n2. Вася\n3. Петя'


assert winners_list(10, 5, 7) == (
    '1. Петя\n'
    '2. Толя\n'
    '3. Вася'
)
assert winners_list(5, 7, 10) == (
    '1. Толя\n'
    '2. Вася\n'
    '3. Петя'
)
assert winners_list(10, 10, 5) == (
    '1. Петя\n'
    '2. Вася\n'
    '3. Толя'
)
assert winners_list(10, 10, 10) == (
    '1. Петя\n'
    '2. Вася\n'
    '3. Толя'
)


if __name__ == "__main__":
    p_speed: int = int(input())
    v_speed: int = int(input())
    t_speed: int = int(input())
    print(winners_list(p_speed, v_speed, t_speed))
