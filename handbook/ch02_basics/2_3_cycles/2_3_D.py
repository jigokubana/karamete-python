"""
2.3.C - Считалочка.
Сложность: Time O(N), Space O(1)
"""


"""
Выводит все числа от начала до конца (включительно),
записанные через пробел.
"""
k = int(input())
n = int(input())
if k < n:
    for i in range(k, n + 1):
        print(i, end=' ')
else:
    for i in range(k, n - 1, -1):
        print(i, end=' ')
