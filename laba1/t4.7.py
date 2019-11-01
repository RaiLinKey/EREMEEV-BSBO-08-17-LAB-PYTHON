min_ukaz = 0
x = int(input('Введите x: '))
y = int(input('Введите y: '))
coord = [0, 0]
direction = input('Введите направление (север, юг, запад, восток, стоп): ')
if x == 0 and y == 0:
    print(0)
while direction.lower() != 'стоп':
    steps = int(input('Введите количество шагов: '))
    min_ukaz += 1
    if direction.lower() == 'север':
        coord[0] += steps
    elif direction.lower() == 'запад':
        coord[1] -= steps
    elif direction.lower() == 'юг':
        coord[0] -= steps
    elif direction.lower() == 'восток':
        coord[1] += steps
    if int(x) == coord[0] and int(y) == coord[1]:
        print('Минимальное количство указаний: ', min_ukaz)
        break
    direction = input('Введите направление (север, юг, запад, восток, стоп): ')
