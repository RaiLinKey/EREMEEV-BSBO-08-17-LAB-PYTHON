import random
a = 1
b = 1000
random.seed(version=2)
for i in range(1, 11):
    r = random.randint(a, b)
    print(r)
    znak = input()
    if znak == '<':
        b = r
    elif znak == '>':
        a = r
    elif znak == '=':
        print('Я угадал число :)')
        break
    else:
        print('Введено неверное значение!')
        break
    if i == 10:
        print('Мне не удалось угадать число :(')
