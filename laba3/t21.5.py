def fractal_print(obj):
    obj.insert(1, obj)
    obj[1] = obj[:]
    return obj


length = int(input('Введите длину фактала:'))
print('Введите фрактал:')
fractal = []
for i in range(length):
    fractal.append(int(input()))
print(fractal_print(fractal))
