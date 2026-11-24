"""
2.3.G - НОК.
Сложность: Time O(log N), Space O(1).
"""


"""Выводит одно натуральное число – НОК двух данных чисел."""
a = int(input())
b = int(input())
a1 = a
b1 = b
while b:
    a, b = b, a % b
print(b1 * (a1 // a))
