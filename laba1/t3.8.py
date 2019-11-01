a = input('Введите трёхзначное число: ')
b = list(a)

n1 = int(b[0]) + int(b[1])
n2 = int(b[1]) + int(b[2])

if n1 < n2:
    print('Новое число: ' + str(n2) + str(n1))
else:
    print('Новое число: ' + str(n1) + str(n2))
