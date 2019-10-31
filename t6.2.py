ksl = int(input('Введите количество слоёв: '))
for i in range(1, ksl + 1):
    kst = ksl + 1 - i
    print()
    while kst > 0:
        if kst > 1:
            print(' ', end='')
            kst -= 1
        elif kst == 1:
            for j in range(1, i + 1):
                print('* ', end='')
            kst -= 1
