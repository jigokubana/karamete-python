"""
2.3.N - Простая задача.
Сложность: Time O(N), Space O(1).
"""


from math import isqrt
"""Если у числа 2 делителя - выводит 'YES', если нет - 'NO'."""

n = int(input())
is_prime = n >= 2
for d in range(2, isqrt(n) + 1):
    if n % d == 0:
        is_prime = False
        break

print("YES" if is_prime else "NO")
