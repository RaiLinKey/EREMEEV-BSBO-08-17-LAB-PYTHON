n = int(input('Введите количество записей: '))
zap = [['0' for x in range(3)] for y in range(n)]
for m in range(n):
    zap[m][0] = input('Имя: ')
    zap[m][1] = input('День: ')
    zap[m][2] = input('Месяц: ')

print(zap)
