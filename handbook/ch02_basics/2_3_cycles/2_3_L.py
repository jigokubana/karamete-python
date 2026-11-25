"""
2.3.L - Сильная цифра.
Сложность: Time O(log N), Space O(1).
"""


"""Выводит наибольшее из введённого числа."""
number = int(input())
result: list[int] = []
while number != 0:
    result.append(number % 10)
    number = number // 10
print(max(result))
