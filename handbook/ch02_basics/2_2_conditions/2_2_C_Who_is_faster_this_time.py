"""
2.2.C - Кто быстрее на этот раз?
Сложность: Time 0(1), Space 0(1).
"""


def race_winner(p_speed: float, v_speed: float, t_speed: float) -> str:
    """Находит победителя гонки путём сравнения"""
    if p_speed > v_speed and p_speed > t_speed:
        return 'Петя'
    elif v_speed > p_speed and v_speed > t_speed:
        return 'Вася'
    else:
        return 'Толя'


assert race_winner(10, 5, 7) == 'Петя'
assert race_winner(5, 7, 10) == 'Толя'
assert race_winner(5, 10, 7) == 'Вася'


if __name__ == "__main__":
    p_speed: float = float(input())
    v_speed: float = float(input())
    t_speed: float = float(input())
    print(race_winner(p_speed, v_speed, t_speed))
