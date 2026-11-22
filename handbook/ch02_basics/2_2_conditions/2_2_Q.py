"""
2.2.Q - Корень зла.
Сложность: Time O(1), Space O(1).
"""


#import math
def koren(a: int, b: int, c: int) -> float:
#   discriminant = b ** 2 - 4 * a * c
    return b ** 2 - 4 * a * c


if __name__ == "__main__":
    a: int = int(input())
    b: int = int(input())
    c: int = int(input())
    print(koren(a, b, c))
