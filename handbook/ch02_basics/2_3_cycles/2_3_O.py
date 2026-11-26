"""
2.3.O - Зайка 4.
Сложность: Time O(N), Space O(1).
"""


n = int(input())
zaika_count = 0
for i in range(n):
    landscape = input()
    if 'зайка' in landscape:
        zaika_count = zaika_count + 1
    else:
        continue
print(zaika_count)
