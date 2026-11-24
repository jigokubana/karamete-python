"""
2.3.E - Внимание! Акция!
Сложность: Time O(N), Space O(1).
"""


"""Считает сумму товаров, если число >= 500 - применяет скидку 10%."""
result = 0
while (number := float(input())) != 0:
    if number >= 500:
        number = number - number / 10
        result = result + number
    else:
        result = result + number
else:
    print(f'{result}')
