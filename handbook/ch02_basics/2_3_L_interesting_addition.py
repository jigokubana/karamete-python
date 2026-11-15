"""
Задача: 2.3.L - Интересное сложение.
Сложность: Time 0(1), Space 0(1).
"""


def sum_numbers(first_number: int, second_number: int) -> int:
    """Складывает два числа поразрядно без учёта переносов."""
    if first_number // 100 > 0:
        first_digit = first_number // 100
        second_digit = first_number % 100 // 10
        third_digit = first_number % 10
    else:
        first_digit = 0
        second_digit = first_number % 100 // 10
        third_digit = first_number % 10
    if second_number // 100 > 0:
        fourth_digit = second_number // 100
        fifth_digit = second_number % 100 // 10
        sixth_digit = second_number % 10
    else:
        fourth_digit = 0
        fifth_digit = second_number % 100 // 10
        sixth_digit = second_number % 10

    if (first_digit + fourth_digit) % 10 > 0:
        first_pair = (first_digit + fourth_digit) % 10
    else:
        first_pair = 0
    if (second_digit + fifth_digit) % 10 > 0:
        second_pair = (second_digit + fifth_digit) % 10
    else:
        second_pair = 0
    if (third_digit + sixth_digit) % 10 > 0:
        third_pair = (third_digit + sixth_digit) % 10
    else:
        third_pair = 0
    return int(f'{first_pair}{second_pair}{third_pair}')


assert sum_numbers(123, 99) == 112
assert sum_numbers(45, 69) == 4


if __name__ == "__main__":
    first_number: int = int(input())
    second_number: int = int(input())
    print(sum_numbers(first_number, second_number))