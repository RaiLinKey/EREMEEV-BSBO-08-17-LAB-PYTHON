n = int(input('Введите ширину: '))
m = int(input('Введите высоту: '))
while True:
    symb = input('Введите символ: ')
    if len(symb) > 1:
        print('Введено больше одного символа')
    else:
        break
for j in range(1, m + 1):
    if j == 1 or j == m:
        for h in range(1, n + 1):
            print(symb + ' ', end='')
        print()
    else:
        print(symb + ' ', end='')
        for l in range(2, n):
            print('  ', end='')
        print(symb)
