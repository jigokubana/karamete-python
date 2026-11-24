"""
2.1.S - Украшение чека.
Сложность: Time O(1), Space O(1).
"""


def receipt_maker(
    item_name: str,
    item_cost: int,
    weight: int,
    user_money_amount: int,
) -> str:
    """Формирует отформатированный кассовый чек шириной 35 символов."""
    caption: str = "Чек"
    total: int = item_cost * weight
    change: int = user_money_amount - total
    price_str: str = f"{weight}кг * {item_cost}руб/кг"
    total_str: str = f"{total}руб"
    paid_str: str = f"{user_money_amount}руб"
    change_str: str = f"{change}руб"
    border: str = "=" * 35
    return (
        f"{caption:=^35}\n"
        f"Товар:{item_name:>29}\n"
        f"Цена:{price_str:>30}\n"
        f"Итого:{total_str:>29}\n"
        f"Внесено:{paid_str:>27}\n"
        f"Сдача:{change_str:>29}\n"
        f"{border}"
    )


assert receipt_maker("черешня", 2, 3, 10) == (
    "================Чек================\n"
    "Товар:                      черешня\n"
    "Цена:                 3кг * 2руб/кг\n"
    "Итого:                         6руб\n"
    "Внесено:                      10руб\n"
    "Сдача:                         4руб\n"
    "==================================="
)
assert receipt_maker("манго", 187, 43, 8041) == (
    "================Чек================\n"
    "Товар:                        манго\n"
    "Цена:              43кг * 187руб/кг\n"
    "Итого:                      8041руб\n"
    "Внесено:                    8041руб\n"
    "Сдача:                         0руб\n"
    "==================================="
)


if __name__ == "__main__":
    item_name: str = input()
    item_cost: int = int(input())
    weight: int = int(input())
    user_money_amount: int = int(input())
    print(receipt_maker(item_name, item_cost, weight, user_money_amount))
