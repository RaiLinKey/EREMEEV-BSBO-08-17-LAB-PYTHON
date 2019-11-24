dx = int(input('Введите длину поля: '))
dy = int(input('Введите высоту поля: '))
# Создаём матрицу pole и заполняем её нулями
pole = [[0 for x in range(dx)] for y in range(dy)]
# Заполняем матрицу своими элементами
print('Заполните поле (заполнение происходит слева направо, сверху внизу): ')
for i in range(dy):
    for j in range(dx):
        pole[i][j] = int(input())

k = int(input('Введите количество капель: '))
# Запускаем цикл, нанесения урона каплями
# Сколько капель мы капаем, чтолько раз и повториться этот цикл
for u in range(k):
    # Вводим координаты куда упала капля
    ux = int(input('Введите Х координату капли: '))
    uy = int(input('Введите Y координату капли: '))
    for dmg_y in range(-1, 2):
        # Проверка не упёрлись ли мы в край поля по Y
        if uy + dmg_y < 0:
            continue
        elif uy + dmg_y > dy - 1:
            break
        for dmg_x in range(-1, 2):
            # Проверка не упёрлись ли мы в край поля по Х
            if ux + dmg_x < 0:
                continue
            elif ux + dmg_x > dx - 1:
                break
            # Если у нас целевой элемент, то наносим 8 урона
            if dmg_x == 0 and dmg_y == 0:
                pole[uy][ux] -= 8
            # Иначе наносим 4 урона
            else:
                pole[uy + dmg_y][ux + dmg_x] -= 4

# Конечный вывод матрицы
for i in range(dy):
    for j in range(dx):
        # Если в процессе нанесения урона мы ушли в минус по количеству букашек,
        # то зануляём отрицательные занчения
        if pole[i][j] < 0:
            pole[i][j] = 0
        print(pole[i][j], '', end='')
    print()
