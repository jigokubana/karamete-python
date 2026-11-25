"""
2.3.N - Простая задача.
Сложность: Time O(N), Space O(1).
"""


"""Если у числа 2 делителя - выводит 'YES', если нет - 'NO'."""
n = int(input())
m = 1
result: list[int] = []
while m <= n:
    for i in range(n):
        while m <= n:
            if n % m == 0:
                result.append(m)
                m = m + 1
            else:
                m = m + 1
if len(result) == 2:
    print('YES')
else:
    print('NO')
