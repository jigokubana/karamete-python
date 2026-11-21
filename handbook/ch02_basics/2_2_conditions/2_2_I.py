"""
2.2.I - Первому игроку приготовиться
Сложность: Time: 0(1), Space 0(1).
"""


def turn_analyzer(p_one: str, p_two: str, p_three: str) -> str:
    """По лексикографическому порядку решает, кто будет ходить первым"""
    if p_one <= p_two and p_one <= p_three:
        return p_one
    elif p_two < p_one and p_two < p_three:
        return p_two
    else:
        return p_three


assert turn_analyzer('Вова', 'Аня', 'Боря') == 'Аня'
assert turn_analyzer('Толя', 'коля', 'Вася') == 'Вася'


if __name__ == "__main__":
    player_one: str = input()
    player_two: str = input()
    player_three: str = input()
    print(turn_analyzer(player_one, player_two, player_three))
