def prime(num):
    if num == 1:
        return 'Не является ни простым, ни составным числом'
    else:
        remember = num
        flag = 0
        for i in range(1, remember + 1):
            if remember % i == 0:
                flag += 1
        if flag == 2:
            return 'Простое число'
        else:
            return 'Составное число'


print('Введите число:')
number1 = int(input())
print(prime(number1))
