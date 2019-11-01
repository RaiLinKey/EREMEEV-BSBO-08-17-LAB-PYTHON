pass_code = input('Введите трёхзнаный пароль: ')
if len(set(list(pass_code))) == 3:
    print('Пароль принят!')
elif len(set(list(pass_code))) == 2:
    print('Пароль не принят! Две повторяющихся цифры!')
elif len(set(list(pass_code))) == 1:
    print('Пароль не принят! Три повторяющихся цифры!')
else:
    print('Введены неверные данные')
