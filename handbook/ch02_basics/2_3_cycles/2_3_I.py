"""
2.3.I - Факториал.
Сложность: Time O(N), Space O(1).
"""


"""Выводит факториал введённого числа."""
result = 1
for n in range(2, int(input()) + 1):
    result *= n
print(result)
