login = input('Введите логин: ')
email = input('Введите адрес электронной почты: ')
if '@' in login:
    print('Некоректный логин!')
elif '@' not in email:
    print('Некорректный адрес электронной почты!')
else:
    print('OK')
