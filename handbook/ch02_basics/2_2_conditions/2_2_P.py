"""
2.2.P - Легенды велогонок возвращаются: кто быстрее?
Сложность: Time O(1), Space O(1).
"""


def race_winner(p_speed: int, v_speed: int, t_speed: int) -> str:
    """Сортирует тройку лидеров и собирает пьедестал."""
    s1, n1 = p_speed, 'Петя'
    s2, n2 = v_speed, 'Вася'
    s3, n3 = t_speed, 'Толя'

    if s1 < s2:
        s1, s2 = s2, s1
        n1, n2 = n2, n1
    if s2 < s3:
        s2, s3 = s3, s2
        n2, n3 = n3, n2
    if s1 < s2:
        s1, s2 = s2, s1
        n1, n2 = n2, n1

    return (
        f'{"":8}{n1:^8}\n'
        f'{n2:^8}\n'
        f'{"":16}{n3:^8}\n'
        f'{"II":^8}{"I":^8}{"III":^8}'
    )


assert race_winner(10, 5, 7) == (
    f'{"":8}{"Петя":^8}\n'
    f'{"Толя":^8}\n'
    f'{"":16}{"Вася":^8}\n'
    f'{"II":^8}{"I":^8}{"III":^8}'
)
assert race_winner(5, 7, 10) == (
    f'{"":8}{"Толя":^8}\n'
    f'{"Вася":^8}\n'
    f'{"":16}{"Петя":^8}\n'
    f'{"II":^8}{"I":^8}{"III":^8}'
)


if __name__ == "__main__":
    p_speed: int = int(input())
    v_speed: int = int(input())
    t_speed: int = int(input())
    print(race_winner(p_speed, v_speed, t_speed))
