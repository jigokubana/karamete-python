"""
2.3.K - Цифровая сумма.
Сложность: Time O(log N), Space O(1).
"""


"""Выводит сумму цифр исходного числа."""
number = int(input())
result = 0
while number != 0:
    result = result + number % 10
    number = number // 10
print(result)
