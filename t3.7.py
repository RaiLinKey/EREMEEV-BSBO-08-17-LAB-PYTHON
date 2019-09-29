a = input('Введите трёхзначное число: ')
b = list(a)

v_max = float(b[0])
v_min = float(b[0])
if v_max < float(b[1]):
    v_max = float(b[1])
if v_max < float(b[2]):
    v_max = float(b[2])
if v_min > float(b[1]):
    v_min = float(b[1])
if v_min > float(b[2]):
    v_min = float(b[2])

half_sum = (v_min + v_max) / 2
if half_sum == float(b[0]):
    print('Вы ввели красивое число')
elif half_sum == float(b[1]):
    print('Вы ввели красивое число')
elif half_sum == float(b[2]):
    print('Вы ввели красивое число')
else:
    print('Увы, число не красивое')
