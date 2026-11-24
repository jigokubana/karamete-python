"""
2.3.F - НОД.
Сложность: Time O(log N), Space O(1).
"""


"""Выводит одно натуральное число – НОД двух данных чисел."""
a = int(input())
b = int(input())
while b:
    a, b = b, a % b
print(a)
