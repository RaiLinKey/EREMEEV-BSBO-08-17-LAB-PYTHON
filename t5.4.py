import random

num = int(input('Количество камней в куче: '))
turn = 0
while num > 0:
    turn += 1
    if turn % 2 == 1:
        print('Ход ИИ')
        num -= random.randint(1, 3)
    elif turn % 2 == 0:
        while True:
            kk = int(input('Количство камней: '))
            if kk in range(1, 4):
                break
            else:
                print('Введено неверное значение. Повторите попытку.\n')
                continue
        num -= kk
    if num < 0:
        num = 0
    print('Количество камней в конце хода:', num, '\n')

if turn % 2 == 1:
    print('Победил ИИ')
else:
    print('Вы победили')
