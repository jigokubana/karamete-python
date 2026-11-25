"""
2.3.J - Маршрут построен.
Сложность: Time O(N), Space O(1).
"""


"""Выводит координаты конечной точки маршрута."""
x = 0
y = 0
while (location := input()) != 'СТОП':
    steps = int(input())
    if location == 'СЕВЕР':
        y += steps
    elif location == 'ВОСТОК':
        x += steps
    elif location == 'ЮГ':
        y -= steps
    elif location == 'ЗАПАД':
        x -= steps

print(y)
print(x)
