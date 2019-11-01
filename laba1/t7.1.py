kol = int(input('Введите кол-во строк: '))
s = 0
while kol != 0:
    stroka = input()
    if 'Кот' in stroka or 'кот' in stroka:
        s = s + 1
    kol = kol - 1
if s != 0:
    print('Мяу')
else:
    print('Нет')
