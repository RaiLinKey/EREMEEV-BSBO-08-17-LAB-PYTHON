string = input('Введите строку: ')
sbs = list(set(string.lower()))
l_string = len(string)
l_sbs = len(sbs)
max_inputs = 0

for i in range(l_sbs):
    n = 0
    for j in range(l_string):
        if string[j] == sbs[i]:
            n += 1
    if n > max_inputs:
        max_inputs = n

print('Максимальное количество вхождений в строку:', max_inputs)
