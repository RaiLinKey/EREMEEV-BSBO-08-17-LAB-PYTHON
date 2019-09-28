a = input('Введите трёхзначное число: ')
b = list(a)
x1 = float(b[0])
x2 = float(b[1])
x3 = float(b[2])

v_max = x1
v_min = x1
if v_max < x2:
    v_max = x2
if v_max < x3:
    v_max = x3
if v_min > x2:
    v_min = x2
if v_min > x3:
    v_min = x3

print(v_max, v_min)

half_sum = (v_min + v_max) / 2
if half_sum == x1:
    print('Вы ввели красивое число')
elif half_sum == x2:
    print('Вы ввели красивое число')
elif half_sum == x3:
    print('Вы ввели красивое число')
else:
    print('Увы, число не красивое')
