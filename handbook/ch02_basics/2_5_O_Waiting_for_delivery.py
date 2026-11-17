"""
2.1.O - В ожидании доставки.
Сложность: Time 0(1), Space 0(1).
"""


def clock(hours: int, minutes: int, waiting_time: int) -> str:
    """Переводит часы на время, когда приедет доставка"""
    arriving_time_in_minutes = hours * 60 + minutes + waiting_time
    arriving_time_hours = (arriving_time_in_minutes // 60) % 24
    arriving_time_minutes = arriving_time_in_minutes % 60
    return f'{arriving_time_hours:02d}:{arriving_time_minutes:02d}'


assert clock(8, 0, 65) == '09:05'
assert clock(10, 15, 2752) == '08:07'


if __name__ == "__main__":
    hours: int = int(input())
    minutes: int = int(input())
    waiting_time: int = int(input())
    print(clock(hours, minutes, waiting_time))
