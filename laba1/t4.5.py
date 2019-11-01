num = int(input('Введите число: '))
count = 0
while True:
    if num == 1:
        break
    if num % 2 == 0:
        num /= 2
        count += 1
    elif num % 2 == 1:
        num = num * 3 + 1
        count += 1
    else:
        print('Что-то пошло не так •_•')
        break
print('Число шагов последовательности:', count)
