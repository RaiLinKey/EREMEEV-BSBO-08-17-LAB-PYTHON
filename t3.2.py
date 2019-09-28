print('\nCalculator Very Lite v0.0.1 pre-pre-alpha\n')
n1 = float(input('Введите значение 1: '))
n2 = float(input('Введите значение 2: '))
act = input('Введите действие: ')
scope = ['+', '-', '*', '/']

if act in scope:
    if act == '+':
        print('Ответ: ', n1 + n2)
    elif act == '-':
        print('Ответ: ', n1 - n2)
    elif act == '*':
        print('Ответ: ', n1 * n2)
    elif act == '/':
        if n2 == 0:
            print('888888')
        else:
            print('Ответ: ', n1 / n2)
else:
    print('888888')
