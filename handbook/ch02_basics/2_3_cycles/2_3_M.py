"""
2.3.M - Первому игроку приготовиться 2.0.
Сложность: Time O(N), Space O(1).
"""


"""Записывает участников и выводит того, кто будет ходить первым."""
n = int(input())
result: list[str] = []
for i in range(n):
    result.append(input())
print(min(result))
