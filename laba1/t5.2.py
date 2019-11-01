num = int(input('Введите число: '))
turns = 0
while num > 1:
    if num % 2 == 1:
        num -= 1
    elif num % 2 == 0:
        num //= 2
    turns += 1
print('Минимальное количество ходов: ', turns)
