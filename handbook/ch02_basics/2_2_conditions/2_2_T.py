"""
2.2.T - Зайка - 2.
Сложность: Time 0(1), Space 0(1)
"""


def landscape_analyzer(str1: str, str2: str, str3: str) -> str:
    """Находит лексикографически минимальную строку со словом 'зайка'."""
    best: str = ''
    if 'зайка' in str1:
        best = str1
    if 'зайка' in str2 and (not best or str2 < best):
        best = str2
    if 'зайка' in str3 and (not best or str3 < best):
        best = str3
    return f'{best} {len(best)}'


assert landscape_analyzer(
    'березка елочка зайка волк березка',
    'сосна сосна сосна елочка грибочки медведь',
    'сосна сосна сосна белочка сосна белочка'
) == 'березка елочка зайка волк березка 33'
assert landscape_analyzer(
    'зайка березка',
    'березка зайка',
    'березка елочка березка'
) == 'березка зайка 13'


if __name__ == "__main__":
    str1: str = input()
    str2: str = input()
    str3: str = input()
    print(landscape_analyzer(str1, str2, str3))
