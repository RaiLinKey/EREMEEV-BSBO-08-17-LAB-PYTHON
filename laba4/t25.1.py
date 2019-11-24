from string import ascii_letters, digits
from random import choice


def generate_password(n):
    password = []
    while len(password) < n:
        sym = choice(ascii_letters + digits)
        if sym not in password and sym not in ['o', 'O', 'l', '1', 'I', '0']:
            password.append(sym)
    return ''.join(password)


def main(n, m):
    passwords = [generate_password(m) for i in range(n)]
    return passwords


print('Случайный пароль из 7 символов', generate_password(7))
print('10 случайных паролей длиной 15 символов')
print(*main(10, 15), sep='\n')
