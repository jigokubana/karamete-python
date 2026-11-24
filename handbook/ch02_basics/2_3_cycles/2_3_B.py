"""
2.3.B - Зайка - 3.
Сложность: Time O(N * L), Space O(L).
"""


"""Проверяет каждую строку и считает сколько раз замечено слово 'зайка'."""
zaika_check = 0
while (landscape := input()) != 'Приехали!':
    if 'зайка' in landscape:
        zaika_check = zaika_check + 1
else:
    print(f'{zaika_check}')
