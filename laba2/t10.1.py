m = input('Введите слово: ')
n = int(input('Введите число: '))
if n-1 <= len(m):
    print(m[n-1])
else:
    print('ОШИБКА')
