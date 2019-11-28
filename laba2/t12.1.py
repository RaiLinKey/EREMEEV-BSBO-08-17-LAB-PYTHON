n = int(input('Записи белого списка: '))
bs = []
rez = []
while n != 0:
    bs.append(input('Введите запись: '))
    n = n - 1
m = int(input('\nКоличство запросов: '))
zap = []
while m != 0:
    zap.append(input('Введите запрос: '))
    for i in bs:
        if zap[-1] == i:
            rez.append(i)
    m = m - 1

for i in rez:
    print(i)
