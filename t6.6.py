while True:
    n = int(input('Введите число n: '))
    summa = 0
    if n < 0 or n > 1300000:
        print('Число вне диапазона')
        continue
    else:
        for i in range(1, n + 1):
            summa = summa + (1 / (i ** 2))
        otvet = round(((3.141592653589793 ** 2) / summa), 12)
        print(otvet)
        break
