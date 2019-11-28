def ask_password():
    password = 'password'
    for k in range(3):
        word = input()
        if word == password:
            print('Пароль принят')
            break
        elif k == 2:
            print('В доступе отказано')


ask_password()
