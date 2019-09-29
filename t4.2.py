print('Вводите наблюдаемую температуру. Чтобы прекратить ввод напишите сило меньше -300.\n')
avg = []
while True:
    a = input()
    if float(a) <= -300:
        break
    avg.append(float(a))
print('\nСредняя температура: ' + str(float(sum(avg)) / max(len(avg), 1)))
