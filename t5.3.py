num1 = int(input('Количество камней в 1 куче: '))
num2 = int(input('Количество камней во 2 куче: '))
num = [num1, num2]
while (num[0] > 0) | (num[1] > 0):
    nk = int(input('\nБерём из кучи: '))
    kk = int(input('Количество камней: '))
    if kk > num1:
        print('Неверное значение')
        continue
    else:
        num[nk-1] -= kk
    print('\nКамней в конце хода:\nПервая куча:', num[0], '\nВторая куча:', num[1])
