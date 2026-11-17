"""
2.2.A - Просто здравствуй, просто как дела
Сложность: Time 0(1), Space 0(1)
"""


if __name__ == "__main__":
    name: str = input('Как Вас зовут?\n')
    print(f'Здравствуйте, {name}!')
    state: str = input('Как дела?\n')
    if state == 'хорошо':
        print('Я за Вас рада!')
    else:
        print('Всё наладится!')
