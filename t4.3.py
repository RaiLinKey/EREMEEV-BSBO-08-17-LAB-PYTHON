from math import log

num = int(input('Введите число: '))

if log(num, 2).is_integer():
    print(log(num, 2))
else:
    print('НЕТ')
