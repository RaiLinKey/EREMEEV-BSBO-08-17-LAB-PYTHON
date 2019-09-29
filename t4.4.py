pass1 = input('Введите пароль: ')
pass2 = input('Повторите пароль: ')

if len(pass1) < 8:
    print('Короткий пароль!')
elif '123' in pass1:
    print('Слишком простой пароль!')
elif pass1 != pass2:
    print('Пароли не совпадают!')
else:
    print('ОК')
