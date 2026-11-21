"""
2.2.J - Лучшая защита - шифрование.
Сложность: Time O(1), Space O(1).
"""


def encrypter(number: int) -> str:
    """Шифрует число"""
    a = number // 100
    b = number // 10 % 10
    c = number % 10
    step_one = b + c
    step_two = a + b
    if step_one > step_two:
        return f'{step_one}{step_two}'
    else:
        return f'{step_two}{step_one}'


assert encrypter(123) == '53'
assert encrypter(741) == '115'


if __name__ == "__main__":
    number: int = int(input())
    print(encrypter(number))
