"""
2.2.H - Зайка - 1.
Сложность: Time 0(1), Space 0(1).
"""


def word_finder(line: str) -> str:
    """Проверяет есть ли в строке слово 'зайка'"""
    if 'зайка' in line:
        return 'YES'
    else:
        return 'NO'


assert word_finder('березка елочка зайка волк березка') == 'YES'
assert word_finder('сосна сосна сосна елочка грибочки медведь') == 'NO'


if __name__ == "__main__":
    line: str = input()
    print(word_finder(line))
